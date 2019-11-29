import unittest
from logo_crawler.logo_finder import LogoFinder
from logo_crawler.html_page import HTMLPage


class TestLogoFinder(unittest.TestCase):

    def test_it_returns_none_not_found_signatures(self):
        html_page = HTMLPage()
        html_page.url = "test"
        html_page.text = "<html><body><body></html>"
        logo_finder = LogoFinder()
        logo = logo_finder.search(html_page)
        self.assertIsNone(logo)

    def test_it_returns_logo_if_matches_rule(self):
        logo_link = "http://test/logo.png"
        html_page = HTMLPage()
        html_page.url = "test"
        html_page.text = "<html><body><img alt='logo' src='http://test/logo.png'><body></html>"
        logo_finder = LogoFinder()
        logo = logo_finder.search(html_page)
        self.assertEquals(logo_link, logo)


if __name__ == '__main__':
    unittest.main(verbosity=2)
