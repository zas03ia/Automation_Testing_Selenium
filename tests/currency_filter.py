import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

currency_dict = {
    "USD": "$",
    "CAD": "$",
    "EUR": "€",
    "GBP": "£",
    "AUD": "$",
    "SGD": "$",
    "AED": "د.إ.",
    "BDT": "৳",
}


def test_currency_filter(driver, url):
    """
    Tests the functionality of each currency filter on the webpage.

    This function navigates to a specified URL, interacts with the currency
    dropdown menu in the footer section, and verifies whether the displayed
    prices update correctly based on each of the selected currencies.

    """

    driver.get(url)

    try:
        # Scroll down to the footer section
        footer_element = driver.find_element(By.ID, "footer")
        ActionChains(driver).move_to_element(footer_element).perform()

        # Wait for the currency dropdown to become visible
        currency_dropdown = WebDriverWait(footer_element, 10).until(
            EC.visibility_of_element_located((By.ID, "js-currency-sort-footer"))
        )

        # Click the currency dropdown to reveal options
        driver.execute_script("arguments[0].click();", currency_dropdown)

        # Get all currency options within the dropdown parent element
        dropdown_content = driver.find_element(By.CSS_SELECTOR, ".select-ul")
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_content)

        currency_options = WebDriverWait(dropdown_content, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".select-wrap .select-ul li")
            )
        )
        results = []
        # Iterate through each currency option
        for option in currency_options:
            try:
                # Get the currency text
                currency_name = option.get_attribute("data-currency-country")

                # Scroll the option into view and click it
                driver.execute_script("arguments[0].scrollIntoView(true);", option)
                driver.execute_script("arguments[0].click();", option)

                # Allow time for the prices to update
                time.sleep(2)

                # Check if all prices reflect the selected currency
                price_elements = driver.find_elements(
                    By.CLASS_NAME, "price-info js-price-value"
                )

                if not all(
                    currency_dict[currency_name] in price.text
                    for price in price_elements
                ):
                    results.append(
                        [
                            False,
                            f"{currency_name} currency option: failed",
                        ]
                    )
                else:

                    results.append(
                        [
                            True,
                            f"{currency_name} currency option: success",
                        ]
                    )

            except Exception as e:
                return results.append([False, f"Error selecting currency: {str(e)}"])

        return results

    except Exception as e:
        return [[False, f"Error in currency filter test: {str(e)}"]]
