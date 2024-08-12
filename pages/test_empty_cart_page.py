from selene import browser, be, by


class EmptyCart:

    def go_to_cart(self):
        browser.element('[class="sc-eCstlR wQepT header__cart-button"]').click()  #переход в корзину

    def empty_cart(self):
        browser.element(by.partial_text("В корзине пока нет товаров")).should(be.visible)  #проверка пустой корзины

    def add_to_cart(self):
        browser.element('[class="button-children"]').click()  # нажатие в "корзину"

    def start_shopping(self):
        browser.element('[class="sc-eCstlR gPywZE notify-button"]').click()  #кнопка "Начать покупки"


cart = EmptyCart()