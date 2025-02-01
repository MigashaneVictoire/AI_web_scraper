import selenium.webdriver as webdriver
from click import option
from selenium.webdriver.chrome.service import service, Service

# Setup selenium chrome driver
def scrape_site(website):
    print("Launching chrome browser...")

    # Setup selenium webdriver
    driver_path = ""
    options = webdriver.ChromeOptions() # set how chrome should function
    driver = webdriver.Chrome(service=Service(driver_path), options=options)

    try:
        # launch selenium chrom driver site
        driver.get(website)
        print("page loaded!")
        html = driver.page_source # get page source

        return html
    finally:
        driver.quit()

