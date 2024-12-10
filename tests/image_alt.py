from selenium.webdriver.common.by import By


def test_image_alt(driver, url):
    """
    Checks if all <img> elements on the webpage have "alt" attributes.
    """

    driver.get(url)
    images = driver.find_elements(By.TAG_NAME, "img")
    missing_alt = [img for img in images if not img.get_attribute("alt")]
    if missing_alt:
        return [[False, f"{len(missing_alt)} images are missing alt attributes"]]
    return [[True, "All images have alt attributes"]]
