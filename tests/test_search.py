import pytest
from urllib.parse import urlparse, parse_qs
from playwright.sync_api import sync_playwright
from pages.search_page import SearchPage

@pytest.fixture(scope="function")
def search_page(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = SearchPage(page)
    yield search_page
    browser.close()

def test_search_for_python_crash_course(search_page):
    search_page.navigate()
    search_page.search("python crash course")
    expected_query = {'query': ['python crash course'], 'searchType': ['smart']}
    actual_query = parse_qs(urlparse(search_page.page.url).query)
    assert expected_query == actual_query
