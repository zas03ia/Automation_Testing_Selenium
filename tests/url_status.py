import requests

from selenium.webdriver.common.by import By


def test_url_status(driver, url):
    """
    Checks the status of all hyperlinks (<a> tags) on a webpage.

    This function navigates to a given URL, retrieves all <a> tags on the page,
    and verifies whether the hyperlinks are valid by sending HTTP HEAD requests.
    Links returning a 404 status code or causing exceptions are considered broken.
    """

    driver.get(url)
    links = driver.find_elements(By.TAG_NAME, "a")
    results = []
    for link in links:
        href = link.get_attribute("href")
        if href:
            try:
                response = requests.head(href)
                if response.status_code == 404:
                    results.append([False, f"Broken link: {href}"])
                else:
                    results.append([True, f"Valid link: {href}"])
            except Exception:
                results.append([False, f"Broken link: {href}"])
    return results if results else [results]
