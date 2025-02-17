import unittest
import asyncio
from unittest.mock import patch, MagicMock
from pathlib import Path
from main import crawl_documentation

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.test_url = "https://test-docs.example.com"
        self.test_name = "test_docs"
        self.output_dir = Path(f"docs/{self.test_name}")
    
    async def async_setup(self):
        # Create mock crawler result for main page
        self.mock_main_result = MagicMock()
        self.mock_main_result.links = {
            "internal": [
                "https://test-docs.example.com/docs/page1/",
                "https://test-docs.example.com/docs/page2/",
                {"href": "https://test-docs.example.com/docs/page3/"},
            ]
        }
        self.mock_main_result.markdown = "# Main Page\nContent"
        self.mock_main_result.success = True

        # Create mock crawler result for internal pages
        self.mock_page_result = MagicMock()
        self.mock_page_result.markdown = "# Internal Page\nContent"
        self.mock_page_result.success = True
    
    def tearDown(self):
        # Clean up test output directory if it exists
        if self.output_dir.exists():
            # Remove all markdown files recursively
            for file in self.output_dir.glob("**/*.md"):
                file.unlink()
            # Remove subdirectories in reverse order
            for dir in sorted(self.output_dir.glob("**/"), reverse=True):
                if dir != self.output_dir and dir.is_dir():
                    dir.rmdir()
            # Remove the main output directory
            self.output_dir.rmdir()
    
    @patch('main.AsyncWebCrawler')
    async def test_crawl_documentation(self, mock_crawler_class):
        await self.async_setup()
        
        # Configure mock crawler
        mock_crawler = MagicMock()
        mock_crawler.__aenter__.return_value = mock_crawler
        mock_crawler_class.return_value = mock_crawler
        
        # Configure mock crawler.arun() to return different results for main page and internal pages
        async def mock_arun(url, config):
            if url == self.test_url:
                return self.mock_main_result
            return self.mock_page_result
        
        mock_crawler.arun = mock_arun
        
        # Run the crawler
        await crawl_documentation(self.test_url, self.test_name)
        
        # Verify output directory was created
        self.assertTrue(self.output_dir.exists())
        
        # Verify files were created
        expected_files = [
            "index.md",
            "docs/page1/index.md",
            "docs/page2/index.md",
            "docs/page3/index.md"
        ]
        
        for file in expected_files:
            self.assertTrue((self.output_dir / file).exists())
    
    def test_crawl_documentation_sync(self):
        # Helper to run async test
        asyncio.run(self.test_crawl_documentation())

if __name__ == '__main__':
    unittest.main()
