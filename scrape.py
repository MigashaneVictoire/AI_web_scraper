# import selenium.webdriver as webdriver
# from click import option
# from selenium.webdriver.chrome.service import service, Service

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By

# Setup selenium chrome driver
def scrape_site(website):
    print("Launching chrome browser...")

    # Setup selenium webdriver
    driver_path = "./driver/chromedriver"
    options = webdriver.ChromeOptions() # set how chrome should function
    driver = webdriver.Chrome(service=Service(driver_path), options=options)

    try:
        # launch selenium chrom driver site
        driver.get(website)
        print("page loaded!")
        html = driver.page_source # get page source
        time.sleep(10)
        return html
    finally:
        driver.quit()


AUTH = 'brd-customer-hl_54ee2d9e-zone-web_scraper_ai:934gednzq3u0'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'
def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get('https://example.com')
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        print(html)
