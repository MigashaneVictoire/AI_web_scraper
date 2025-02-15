from bs4 import BeautifulSoup
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
import credentials as cred
import time
from bs4 import BeautifulSoup

# bright data credentials
AUTH = cred.authentication()
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

# Setup selenium chrome driver
def scrape_site(website):
    print('Connecting to Scraping Browser...')
    # brightdata set up
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website) #lunch website

        # CAPTION Handling
        print("waiting caption to solve...")
        solve_cap = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })

        # print('Captcha solve status:', solve_cap['value']['status'])
        print('Navigated! Scrapping page content...')
        html = driver.page_source
        time.sleep(2)
        return html


def body_content_extraction(html_trafic):
    soup = BeautifulSoup(html_trafic, "html.parser")
    body_html = soup.body
    if body_html:
        return str(body_html)
    else:
        return ""

# clean the html content
def clean_content(body_html):
    soup = BeautifulSoup(body_html, "html.parser")

    # remove script and style contents
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()

    # remove empty text strings | remove \n and leading and trailing spaces
    cleaned_content = soup.get_text(separator= "\n")
    cleaned_content= "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

# deal with the token limit
def separate_dom_content(dom_content, max_len=6000):
    # create bashes of 6000 elements in length
    # grap the first 6000 elements and loop starting at the 6001 and count another 6000 elements...
    # until it grabs all the elements on the page
    return [
        dom_content[i:i - max_len] for i in range(0, len(dom_content), max_len)
    ]













