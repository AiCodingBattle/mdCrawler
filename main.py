import os
import asyncio
import logging
import yaml
from pathlib import Path
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def get_safe_filename(url: str) -> str:
    """Convert URL to a safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path:
        return 'index.md'
    
    # Replace unsafe characters
    safe_name = path.replace('/', '_').replace('\\', '_')
    return f"{safe_name}.md"

def get_url_from_link(link) -> str:
    """Extract URL from a link object."""
    if isinstance(link, str):
        return link
    elif isinstance(link, dict):
        return link.get('href', '')
    return ''

def should_process_url(url: str, base_domain: str) -> bool:
    """Determine if a URL should be processed based on filtering rules."""
    parsed = urlparse(url)
    
    # Skip if not from same domain
    if parsed.netloc != base_domain:
        return False
        
    # Skip fragment URLs
    if '#' in url:
        return False
        
    # For Django docs, skip old versions (customize per documentation site)
    if 'djangoproject.com' in base_domain:
        path_parts = parsed.path.strip('/').split('/')
        if len(path_parts) >= 2 and path_parts[0] == 'en':
            try:
                version = float(path_parts[1])
                if version < 4.0:  # Only process Django 4.0+ docs
                    return False
            except ValueError:
                pass
    
    return True

async def crawl_documentation(url: str, name: str, timeout: int = 1800):  # 30 minute timeout
    """
    Crawl a documentation website and save all pages as markdown files.
    
    Args:
        url (str): The URL of the documentation website
        name (str): Name of the output directory where markdown files will be saved
        timeout (int): Maximum time in seconds to spend crawling (default: 30 minutes)
    """
    logger.info(f"Starting crawl process for URL: {url}")
    logger.info(f"Output will be saved in: docs/{name}")

    # Create output directory
    output_dir = Path(f"docs/{name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Created output directory: {output_dir}")

    start_time = datetime.now()
    
    # Configure browser for better performance and reliability
    browser_cfg = BrowserConfig(
        headless=True
    )
    
    # Configure crawler with less restrictive filtering
    link_extraction_cfg = CrawlerRunConfig(
        word_count_threshold=0,  # No minimum word count for link extraction
        excluded_tags=[],  # Don't exclude any tags for link discovery
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.1),  # Very permissive threshold
            options={"ignore_links": False}
        ),
        cache_mode="BYPASS"
    )

    content_extraction_cfg = CrawlerRunConfig(
        word_count_threshold=15,  # Higher threshold to filter small text blocks like menus
        excluded_tags=[
            # Base HTML elements
            "script", "style", "nav", "header", "footer", "aside",
            # Navigation and menu selectors
            ".sidebar", "#sidebar", ".menu", "#menu", ".navigation", "#navigation",
            # Documentation specific selectors
            "[role='navigation']", ".nav-menu", ".nav-list", ".table-of-contents",
            ".toc", "#toc", ".site-nav", ".site-menu", ".docs-nav", ".docs-menu",
            # Specific to documentation platforms
            # Mintlify (firecrawl)
            ".mintlify-nav", ".docs-sidebar", ".navigation-menu", ".nav-groups",
            ".nav-wrapper", ".nav-container", ".navigation-wrapper",
            # MkDocs (crawl4ai)
            ".md-nav", ".md-sidebar", ".md-header", ".md-footer", ".md-tabs",
            ".md-search", ".md-search-result", ".md-source", ".md-header-nav",
            ".md-main__inner > nav", ".md-nav__title", ".md-nav__list",
            ".terminal-mkdocs", ".terminal-mkdocs-nav", ".terminal-mkdocs-sidebar",
            # Generic doc elements
            ".search-box", ".search-wrapper", ".ctrl-key", ".keyboard-shortcut",
            ".version-selector", ".version-info", ".metadata-bar",
            # Additional navigation patterns
            "*[class*='sidebar']", "*[class*='navigation']", "*[class*='nav-']",
            "*[id*='sidebar']", "*[id*='navigation']", "*[id*='nav-']",
            "*[class*='menu']", "*[id*='menu']"
        ],
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.3),
            options={
                "ignore_links": True,
                "ignore_navigation": True,
                "main_content_only": True,
                "remove_navigation_elements": True,
                "clean_documentation_artifacts": True,
                "strip_empty_headings": True,
                "remove_duplicate_content": True
            }
        ),
        cache_mode="BYPASS"
    )
    
    # Initialize crawler
    logger.info("Initializing AsyncWebCrawler...")
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        try:
            # Get base domain for filtering
            base_domain = urlparse(url).netloc
            logger.info(f"Base domain: {base_domain}")
            
            # First get all links from the main page with less restrictive config
            main_result = await crawler.arun(url, config=link_extraction_cfg)
            internal_links = main_result.links.get("internal", [])
            logger.info(f"Found {len(internal_links)} internal links")
            
            # Process the main page with content config
            main_content = await crawler.arun(url, config=content_extraction_cfg)
            main_filename = get_safe_filename(url)
            main_path = output_dir / main_filename
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(main_content.markdown)
            logger.info(f"Saved main page: {main_path}")
            
            # Process each internal link
            processed_urls = {url}  # Keep track of processed URLs to avoid duplicates
            
            for link in internal_links:
                # Check timeout
                if (datetime.now() - start_time).total_seconds() > timeout:
                    logger.warning(f"Timeout reached after {timeout} seconds. Stopping crawl.")
                    break

                try:
                    link_url = get_url_from_link(link)
                    if not link_url or link_url in processed_urls:
                        continue
                        
                    if not should_process_url(link_url, base_domain):
                        logger.debug(f"Skipping filtered URL: {link_url}")
                        continue
                    
                    logger.info(f"Processing link: {link_url}")
                    
                    # Add delay between requests to be polite
                    await asyncio.sleep(0.5)  # 500ms delay between requests
                    
                    # Use content extraction config for the actual page content
                    result = await crawler.arun(link_url, config=content_extraction_cfg)
                    
                    if result and result.success:
                        filename = get_safe_filename(link_url)
                        output_path = output_dir / filename
                        
                        with open(output_path, "w", encoding="utf-8") as f:
                            f.write(result.markdown)
                        logger.info(f"Successfully saved: {output_path}")
                        processed_urls.add(link_url)
                    else:
                        logger.warning(f"Failed to process {link_url}")
                        
                except Exception as e:
                    logger.error(f"Error processing link {link}: {str(e)}")
                    continue
            
            logger.info(f"Total pages processed: {len(processed_urls)}")
            
        except Exception as e:
            logger.error(f"Error during crawling: {str(e)}")
            raise

    logger.info(f"Crawling completed. Output directory: {output_dir}")

async def crawl_multiple_libraries(config_file: str):
    """
    Crawl multiple documentation websites based on a configuration file.
    
    Args:
        config_file (str): Path to the YAML configuration file containing library definitions
    """
    logger.info(f"Loading library configuration from: {config_file}")
    
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading configuration file: {str(e)}")
        raise

    if not config or 'libraries' not in config:
        raise ValueError("Invalid configuration file: 'libraries' section not found")

    libraries = config['libraries']
    if not libraries:
        logger.warning("No libraries defined in configuration file")
        return

    total_libraries = len(libraries)
    for idx, library in enumerate(libraries, 1):
        if not isinstance(library, dict) or 'name' not in library or 'url' not in library:
            logger.warning(f"Skipping invalid library entry: {library}")
            continue

        name = library['name']
        url = library['url']
        
        logger.info(f"\n{'='*50}")
        logger.info(f"Processing library {idx}/{total_libraries}: {name}")
        logger.info(f"{'='*50}")
        
        try:
            await crawl_documentation(url, name)
        except Exception as e:
            logger.error(f"Error processing library {name}: {str(e)}")
            logger.error("Moving to next library...")
            # Sleep for a few seconds before trying the next library
            await asyncio.sleep(5)
            continue

    logger.info(f"\nCompleted processing all libraries ({total_libraries} total)")
    logger.info("Check the 'docs' directory for the generated documentation")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Crawl documentation and convert to markdown")
    parser.add_argument("--config", help="Path to libraries configuration file (YAML)")
    parser.add_argument("--url", help="URL of a single documentation website")
    parser.add_argument("--name", help="Name of the output directory for single website")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    try:
        if args.config:
            # Process multiple libraries from config file
            asyncio.run(crawl_multiple_libraries(args.config))
        elif args.url and args.name:
            # Process single library with direct parameters
            asyncio.run(crawl_documentation(args.url, args.name))
        else:
            parser.error("Either --config or both --url and --name must be provided")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main()