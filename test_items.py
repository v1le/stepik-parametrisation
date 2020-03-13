URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_basket_button_visible(browser):
    browser.get(URL)
    browser.find_element_by_class_name('btn-add-to-basket')
    assert True

