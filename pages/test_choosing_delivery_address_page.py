import allure

from selene import browser, be, by


class DeliveryAddress:
    def ready_meals(self):
        with allure.step('Нажать на кнопку Готовая еда'):
            browser.element('[class="Box-sc-149qidf-0 cuNYME"]').click()

    def add_product(self):
        with allure.step('Нажать - Добавить товар в корзину'):
            browser.element('[class="sc-fmlJrY kmCYRp"]').click()

    def check_text(self):
        with allure.step('Проверить текст'):
            browser.element(by.partial_text("Укажите свой адрес")).should(be.visible)

    def list_of_addresses(self):
        with allure.step('Выбрать самовызов и адрес списком'):
            browser.element('[class="sc-gTgzoy fqqyFT"]').click()
            browser.element('[class="sc-gTgzoy cBxCrY"]').click()

    def address_selection(self):
        with allure.step('Кликнуть по строке поиска и выбрать адрес'):
            browser.element(
                '[class="react-select__value-container react-select__value-container--has-value css-1hwfws3"]').click()
            browser.element('[class="sc-khAkCZ sc-jgHCSr kRZgMU jvIplC"]').click()

    def confirmation(self):
        with allure.step('Нажать "Подтвердить"'):
            browser.element('[class="sc-eCstlR gPywZE focused-shop-submit"]').click()


delivery_address = DeliveryAddress()
