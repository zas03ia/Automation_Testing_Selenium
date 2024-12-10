from selenium.webdriver.common.by import By


def test_image_alt(driver, url):
    """
    Checks if all <img> elements on the webpage have "alt" attributes.
    """

    driver.get(url)
    images = driver.find_elements(By.TAG_NAME, "img")
    results = []
    for img in images:
        if not img.get_attribute("alt"):
            results.append(
                [
                    False,
                    f"src: {img.get_attribute('src')}",
                ]
            )

        else:
            results.append([True, f"src: {img.get_attribute('src')}"])
    return results if results else [results]
