from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
import credentials as cred
import time

AUTH = cred.authentication()
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

# Setup selenium chrome driver
def scrape_site(website):
    print('Connecting to Scraping Browser...')

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)

        # CAPTION Handling
        print("waiting caption to solve...")
        solve_cap = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })

        # print('Captcha solve status:', solve_cap['value']['status'])
        print('Navigated! Scrapping page content...')
        html = driver.page_source
        time.sleep(10)
        return html