import allure
from selene import browser, be, by


class EmptyCart:

    def go_to_cart(self):
      with allure.step('переход в корзину'):
        browser.element('[class="sc-eCstlR wQepT header__cart-button"]').click()

    def empty_cart(self):
      with allure.step('проверить пустую корзину'):
        browser.element(by.partial_text("В корзине пока нет товаров")).should(be.visible)

    def start_shopping(self):
      with allure.step('нажать "Начать покупки"'):
        browser.element('[class="sc-eCstlR gPywZE notify-button"]').click()


cart = EmptyCart()