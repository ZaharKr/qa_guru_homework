import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=opts)
    yield browser
    browser.quit()


def test_google_web(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert "Google" in driver.title
    assert "google.com" in driver.current_url


def test_github_web(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title
    assert "github.com" in driver.current_url
