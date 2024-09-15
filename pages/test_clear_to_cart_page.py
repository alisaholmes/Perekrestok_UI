import allure

from selene import browser, be, by


class Clear:
    def add_product(self):
        with allure.step('Снова нажать - Добавить товар в корзину'):
            browser.element('[class="sc-eCstlR zzeAM cart-add-button"]').click()

    def go_to_shopping_cart(self):
        with allure.step('Переход в корзину'):
            browser.element('[class="sc-eCstlR djqBVS header__cart-button"]').click()

    def checking_product_availability(self):
        with allure.step('Проверка наличия товара в корзине'):
            browser.element(by.partial_text("1 товар")).should(be.visible)

    def clear_button(self):
        with allure.step('Кликнуть "Очистить"'):
            browser.element('[class="sc-eCstlR djqBVS clear-button"]').click()


clear_cart = Clear()
