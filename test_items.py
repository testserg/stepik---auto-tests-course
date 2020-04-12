import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)
    button = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, '.btn-add-to-basket'))
    )
    assert button.is_displayed(), "button not displayed"
