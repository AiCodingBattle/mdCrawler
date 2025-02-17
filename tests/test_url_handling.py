import os
import unittest
from main import get_safe_filename, get_url_from_link

class TestUrlHandling(unittest.TestCase):
    def test_get_safe_filename(self):
        test_cases = [
            # Root URLs
            ("https://docs.python.org", "index.md"),
            ("https://docs.python.org/", "index.md"),
            
            # Directory URLs
            ("https://docs.python.org/3/", "3/index.md"),
            ("https://docs.python.org/3/library", "3/library/index.md"),
            ("https://docs.python.org/3/library/", "3/library/index.md"),
            
            # File URLs
            ("https://docs.python.org/3/library/index.html", "3/library/index.html.md"),
            ("https://docs.python.org/3/library/functions.html", "3/library/functions.html.md"),
            ("https://docs.python.org/3/library/os.html#module-os", "3/library/os.html.md"),
        ]
        
        for url, expected in test_cases:
            with self.subTest(url=url):
                result = get_safe_filename(url)
                self.assertEqual(result, expected.replace('/', os.path.sep), 
                                f"Failed for URL: {url}\nExpected: {expected}\nGot: {result}")
    
    def test_get_url_from_link(self):
        test_cases = [
            # String URL
            ("https://example.com", "https://example.com"),
            # Dict with href
            ({"href": "https://example.com"}, "https://example.com"),
            # Dict without href
            ({"url": "https://example.com"}, ""),
            # Invalid input
            (None, ""),
            (123, ""),
        ]
        
        for input_link, expected in test_cases:
            with self.subTest(input_link=input_link):
                self.assertEqual(get_url_from_link(input_link), expected)

if __name__ == '__main__':
    unittest.main()
