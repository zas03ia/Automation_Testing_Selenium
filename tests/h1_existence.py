from selenium.webdriver.common.by import By


def test_h1_existence(driver, url):
    """
    Checks for the presence of an <h1> tag on the webpage.
    """

    driver.get(url)
    try:
        driver.find_element(By.TAG_NAME, "h1")
        return [[True, "H1 tag exists"]]
    except Exception:
        return [[False, "H1 tag is missing"]]
