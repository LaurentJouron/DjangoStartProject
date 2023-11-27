from selenium import webdriver


def test_my_website_is_online(live_server):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("windows-size=1920x1080")

    driver = webdriver.Chrome(
        executable_path="./tools/chromedriver.exe",
        options=chrome_options,
    )

    driver.get(live_server.url)
    assert driver.title != "Not Found"
