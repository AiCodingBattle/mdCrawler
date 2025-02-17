import os
import asyncio
import logging
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

async def crawl_documentation(url: str, name: str):
    """
    Crawl a documentation website and save all pages as markdown files.
    
    Args:
        url (str): The URL of the documentation website
        name (str): Name of the output directory where markdown files will be saved
    """
    logger.info(f"Starting crawl process for URL: {url}")
    logger.info(f"Output will be saved in: docs/{name}")

    # Create output directory
    output_dir = Path(f"docs/{name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Created output directory: {output_dir}")
    
    # Configure browser for better performance
    browser_cfg = BrowserConfig(
        headless=True,
        viewport_width=1920,
        viewport_height=1080
    )
    
    # Configure crawler with less restrictive filtering
    content_extraction_cfg = CrawlerRunConfig(
        word_count_threshold=0,  # No minimum word count for link extraction
        excluded_tags=["script", "style"],  # Only exclude non-content tags
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.1),  # Very permissive threshold
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
    
    # Initialize crawler
    logger.info("Initializing AsyncWebCrawler...")
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        try:
            # Get base domain for filtering
            base_domain = urlparse(url).netloc
            logger.info(f"Base domain: {base_domain}")
            
            # Process the main page with content config
            main_result = await crawler.arun(url, config=content_extraction_cfg)
            logger.info(f"Main page result: {main_result}")
            logger.info(f"Main page links: {main_result.links}")
            internal_links = main_result.links.get("internal", [])
            logger.info(f"Found {len(internal_links)} internal links")
            logger.info(f"Internal links: {internal_links}")
            
            # Save the main page content
            main_filename = get_safe_filename(url)
            main_path = output_dir / main_filename
            main_path.parent.mkdir(parents=True, exist_ok=True)
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(main_result.markdown)
            logger.info(f"Saved main page: {main_path}")
            
            # Process each internal link
            processed_urls = {url}  # Keep track of processed URLs to avoid duplicates
            
            for link in internal_links:
                try:
                    link_url = get_url_from_link(link)
                    if not link_url or link_url in processed_urls:
                        continue
                        
                    # Skip fragment URLs (URLs with #)
                    if '#' in link_url:
                        logger.debug(f"Skipping fragment URL: {link_url}")
                        continue
                        
                    # Handle relative URLs
                    if not link_url.startswith('http'):
                        # If the link starts with /, it's relative to the domain root
                        if link_url.startswith('/'):
                            link_url = f"http://{base_domain}{link_url}"
                            logger.info(f"Converted root-relative URL to: {link_url}")
                        # Otherwise, it's relative to the current path
                        else:
                            base_path = urlparse(url).path.rsplit('/', 1)[0]
                            link_url = f"http://{base_domain}{base_path}/{link_url}"
                            logger.info(f"Converted relative URL to: {link_url}")
                    
                    # Verify it's from the same domain
                    link_domain = urlparse(link_url).netloc
                    if link_domain != base_domain:
                        logger.debug(f"Skipping external domain: {link_url}")
                        continue
                    
                    logger.info(f"Processing link: {link_url}")
                    filename = get_safe_filename(link_url)
                    logger.info(f"Generated filename: {filename}")
                    
                    logger.info(f"Processing link: {link_url}")
                    # Use content extraction config for the actual page content
                    result = await crawler.arun(link_url, config=content_extraction_cfg)
                    
                    if result and result.success:
                        filename = get_safe_filename(link_url)
                        output_path = output_dir / filename
                        output_path.parent.mkdir(parents=True, exist_ok=True)
                        
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

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Crawl documentation and convert to markdown")
    parser.add_argument("url", help="URL of the documentation website")
    parser.add_argument("name", help="Name of the output directory")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    try:
        asyncio.run(crawl_documentation(args.url, args.name))
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main() 