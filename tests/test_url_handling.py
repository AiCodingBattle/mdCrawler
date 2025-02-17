import unittest
from main import get_safe_filename, get_url_from_link

class TestUrlHandling(unittest.TestCase):
    def test_get_safe_filename(self):
        test_cases = [
            ("https://docs.python.org/3/", "index.md"),
            ("https://docs.python.org/3/library/", "library.md"),
            ("https://docs.python.org/3/library/index.html", "library_index.html.md"),
            ("https://docs.python.org/3/library/functions.html", "library_functions.html.md"),
            ("https://docs.python.org/3/library/os.html#module-os", "library_os.html.md"),
        ]
        
        for url, expected in test_cases:
            with self.subTest(url=url):
                self.assertEqual(get_safe_filename(url), expected)
    
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
