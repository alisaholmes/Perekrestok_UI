from selene import browser, be, by
import allure

class TextChecking:
    def open(self):
      with allure.step('Открыть страницу https://www.perekrestok.ru/  и перейти в каталог'):
        browser.open("cat")

    def sales_go_to_section(self):
      with allure.step('Нажать на кнопку Скидки'):
        browser.element('[class="sc-kstqJO gsLcgV"]').click()

    def product_card(self):
     with allure.step('Перейти в карточку товара'):
        browser.element('[href="/cat/150/p/kartofel-mytyj-2099571"]').click()


    def add_to_cart(self):
      with allure.step('Добавить товар в корзину'):
        browser.element('[class="button-children"]').click()

    def should_have_text(self):
     with allure.step('Проверить текст'):
        browser.element(by.partial_text("Укажите свой адрес")).should(be.visible)


text_checking = TextChecking()
