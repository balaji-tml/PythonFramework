from pages.home_page import HomePage

def test_home_page(driver):

    page = HomePage(driver)

    assert "Selenium Grid Online | Run Selenium Test On Cloud" in driver.title