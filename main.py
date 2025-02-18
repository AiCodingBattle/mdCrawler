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
    """Convert URL to a safe filename.
    
    Args:
        url (str): The URL to convert to a filename
        
    Returns:
        str: A safe filename that preserves the path structure.
        For example:
        - https://docs.python.org/3/ -> index.md
        - https://docs.python.org/3/library/ -> library/index.md
        - https://docs.python.org/3/library/os.html -> library/os.html.md
    """
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    
    # Handle root URL or just domain
    if not path or path == parsed.netloc:
        return 'index.md'
    
    # Remove any URL fragments
    path = path.split('#')[0]
    
    # If path ends with / or has no extension, treat as directory
    if path.endswith('/') or '.' not in Path(path).name:
        # Keep the full path structure for directories
        return f"{path.rstrip('/')}/index.md"
    
    # Add .md extension if not present
    if not path.endswith('.md'):
        path = path + '.md'
    
    # Keep forward slashes for consistency
    return path

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
    
    # Configure crawler with improved filtering and content extraction
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
            content_filter=PruningContentFilter(threshold=0.3),  # Slightly higher threshold for better content quality
            options={
                "ignore_links": False,
                "ignore_navigation": False,
                "main_content_only": False,
                "remove_navigation_elements": False,
                "clean_documentation_artifacts": False,  # Keep all content
                "strip_empty_headings": False,  # Keep all headings
                "remove_duplicate_content": False  # Keep all content
            }
        ),
        cache_mode="BYPASS"
    )
    
    # Initialize crawler with configuration
    crawler = AsyncWebCrawler(
        browser_config=browser_cfg,
        run_config=content_extraction_cfg
    )
    
    try:
        async with crawler:
            logger.info("Crawler initialized successfully")
            
            # Parse base domain for URL filtering
            base_domain = urlparse(url).netloc
            logger.info(f"Base domain for filtering: {base_domain}")
            
            # Process main page first
            main_page = await crawler.process_page(url)
            if not main_page:
                raise Exception(f"Failed to process main page: {url}")
                
            # Save main page content
            main_filename = get_safe_filename(url)
            main_filepath = output_dir / main_filename
            main_filepath.parent.mkdir(parents=True, exist_ok=True)
            main_filepath.write_text(main_page.markdown)
            logger.info(f"Saved main page content to: {main_filepath}")
            
            # Track processed URLs to avoid duplicates
            processed_urls = {url}
            
            # Process all internal links
            for link in main_page.internal_links:
                link_url = get_url_from_link(link)
                if not link_url:
                    continue
                    
                # Skip if already processed or shouldn't be processed
                if link_url in processed_urls or not should_process_url(link_url, base_domain):
                    continue
                    
                logger.info(f"Processing internal link: {link_url}")
                
                try:
                    page = await crawler.process_page(link_url)
                    if page:
                        # Save page content
                        filename = get_safe_filename(link_url)
                        filepath = output_dir / filename
                        filepath.parent.mkdir(parents=True, exist_ok=True)
                        filepath.write_text(page.markdown)
                        logger.info(f"Saved page content to: {filepath}")
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
    
    # Add support for positional arguments
    parser.add_argument("url_pos", nargs="?", help="URL of documentation website (positional)")
    parser.add_argument("name_pos", nargs="?", help="Output directory name (positional)")
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    try:
        if args.config:
            # Process multiple libraries from config file
            asyncio.run(crawl_multiple_libraries(args.config))
        elif args.url and args.name:
            # Process single library with named parameters
            asyncio.run(crawl_documentation(args.url, args.name))
        elif args.url_pos and args.name_pos:
            # Process single library with positional parameters
            asyncio.run(crawl_documentation(args.url_pos, args.name_pos))
        else:
            parser.error("Either --config or URL and name must be provided (either as named or positional arguments)")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
