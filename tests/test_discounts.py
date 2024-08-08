import os
from selene import browser, have, be



def test_discounts():
    browser.open("cat/d")
    browser.element("#product-card__link").element("#/cat/154/p/arbuz-cernyj-princ-bez-kostocek-4071854").click()
    #browser.element("#sc-dlfnuX").click()



