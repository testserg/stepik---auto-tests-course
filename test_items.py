import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket(browser):
    browser.implicitly_wait(2)
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")
