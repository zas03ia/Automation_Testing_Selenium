from selenium.webdriver.common.by import By


def test_h1_sequence(driver, url):
    """
    Verifies the correct sequence of heading tags (h1 to h6) on a webpage.

    This function retrieves all heading tags (h1, h2, h3, h4, h5, h6) on the page and checks if their
    sequence is correct. A correct sequence means that heading tags should follow a numerical order
    with no more than one level difference between consecutive tags (e.g., h1 -> h2 -> h3 -> h2).
    """

    driver.get(url)
    try:
        headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2, h3, h4, h5, h6")
        sequence = [int(h.tag_name[1]) for h in headings]
        if sequence:
            for i in range(0, len(sequence) - 1):
                if abs(sequence[i] - sequence[i + 1]) > 1:
                    return [[False, "Heading tags sequence is broken"]]
            return [[True, "Heading tags sequence is correct"]]
        else:
            return [[True, "No heading tags found"]]
    except Exception:
        return [[False, "Error checking heading tags sequence"]]
