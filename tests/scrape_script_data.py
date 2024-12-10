def scrape_script_data(driver, url):
    """
    Extracts specific data from the `window.ScriptData` object on a webpage.
    """

    driver.get(url)
    try:

        script_data = driver.execute_script(f"return window.ScriptData;")

        data = {
            "SiteURL": script_data.get("config").get("SiteUrl"),
            "CampaignID": script_data.get("pageData").get("CampaignId"),
            "SiteName": script_data.get("config").get("SiteName"),
            "Browser": script_data.get("userInfo").get("Browser"),
            "CountryCode": script_data.get("userInfo").get("CountryCode"),
            "IP": script_data.get("userInfo").get("IP"),
        }

        return data
    except Exception as e:
        return {"Error": "Scraping script data", "Info": str(e)}
