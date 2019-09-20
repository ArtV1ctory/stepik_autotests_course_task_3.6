def test_button_add_to_basket_works(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), \
        'The add to basket button does not exist!'
