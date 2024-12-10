import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from tests import (
    currency_filter,
    h1_existence,
    h1_sequence,
    image_alt,
    url_status,
    scrape_script_data,
)
from utils.save_to_excel import save_to_excel


# Initialize WebDriver
def init_driver(browser="chrome", options=Options()):
    """
    Initializes a Selenium WebDriver for the specified browser.
    """

    if browser == "chrome":
        driver = webdriver.Chrome(options)
    elif browser == "firefox":
        driver = webdriver.Firefox(options)
    else:
        raise ValueError("Unsupported browser")
    return driver


# Main function
def main():
    """
    Main function to run all the automated tests.

    This function calls all the test cases and saves the test results and scraped data to separate Excel files.
    """

    url = "https://www.alojamiento.io/"
    options = Options()
    options.add_argument("--headless")
    driver = init_driver("chrome", options=options)
    test_results = []

    try:
        # Run test cases
        headers = ["page_url", "testcase", "passed", "comments"]
        test_functions = [
            h1_existence.test_h1_existence,
            h1_sequence.test_h1_sequence,
            image_alt.test_image_alt,
            url_status.test_url_status,
            currency_filter.test_currency_filter,
        ]
        for test_func in test_functions:

            driver.get(url)
            test_results = test_func(driver, url)
            df = pd.DataFrame(test_results, columns=["passed", "comments"])
            df = df.assign(page_url=url, testcase=test_func.__name__)[headers]
            save_to_excel(df, f"{test_func.__name__.replace("test_","")}.xlsx")

        # Scrape data from the page
        results = scrape_script_data.scrape_script_data(driver, url)

        df = pd.DataFrame([list(results.values())], columns=list(results.keys()))
        save_to_excel(df, "scrape_script_data.xlsx")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
