import unittest
import asyncio
import aiohttp
from aiohttp import web
import tempfile
from pathlib import Path
from main import crawl_documentation

class TestServer:
    def __init__(self):
        self.app = web.Application()
        self.app.router.add_get('/', self.handle_main)
        self.app.router.add_get('/page1', self.handle_page1)
        self.app.router.add_get('/page2', self.handle_page2)
    
    async def handle_main(self, request):
        html = """
        <!DOCTYPE html>
        <html>
        <head><title>Test Docs</title></head>
        <body>
            <h1>Main Page</h1>
            <p>Welcome to the test documentation.</p>
            <nav>
                <a href="/page1">Page 1</a>
                <a href="/page2">Page 2</a>
            </nav>
        </body>
        </html>
        """
        return web.Response(text=html, content_type='text/html')
    
    async def handle_page1(self, request):
        html = """
        <!DOCTYPE html>
        <html>
        <head><title>Page 1</title></head>
        <body>
            <h1>Page 1</h1>
            <p>This is the first subpage.</p>
            <a href="/">Back to main</a>
        </body>
        </html>
        """
        return web.Response(text=html, content_type='text/html')
    
    async def handle_page2(self, request):
        html = """
        <!DOCTYPE html>
        <html>
        <head><title>Page 2</title></head>
        <body>
            <h1>Page 2</h1>
            <p>This is the second subpage.</p>
            <a href="/">Back to main</a>
        </body>
        </html>
        """
        return web.Response(text=html, content_type='text/html')

class TestIntegration(unittest.TestCase):
    async def async_setup(self):
        # Start test server
        self.server = TestServer()
        runner = web.AppRunner(self.server.app)
        await runner.setup()
        self.site = web.TCPSite(runner, 'localhost', 8080)
        await self.site.start()
        
        # Create temporary directory for output
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = Path(self.temp_dir) / "test_output"
    
    async def async_teardown(self):
        # Stop server
        await self.site.stop()
        
        # Clean up temporary directory
        if self.output_dir.exists():
            for file in self.output_dir.glob("*.md"):
                file.unlink()
            self.output_dir.rmdir()
        Path(self.temp_dir).rmdir()
    
    async def test_crawl_live_server(self):
        await self.async_setup()
        
        try:
            # Run crawler against test server
            await crawl_documentation("http://localhost:8080", "test_output")
            
            # Verify files were created
            expected_files = ["index.md", "page1.md", "page2.md"]
            for file in expected_files:
                file_path = self.output_dir / file
                self.assertTrue(file_path.exists())
                
                # Verify content
                content = file_path.read_text()
                self.assertIn("# ", content)  # Should have at least one heading
                
        finally:
            await self.async_teardown()
    
    def test_crawl_live_server_sync(self):
        # Helper to run async test
        asyncio.run(self.test_crawl_live_server())

if __name__ == '__main__':
    unittest.main()
