from selene import browser, be


class TextChecking:
    def open(self):
        browser.open("cat")  # переход в каталог


    def sales_go_to_section(cls):
        browser.element('[class="sc-kstqJO gsLcgV"]').click()  # нажатие на кнопку "Скидки" и переход в раздел


    def product_card(cls):
        browser.element('[href="/cat/150/p/kartofel-mytyj-2099571"]').click()  # переход в карточку товара


    def add_to_cart(cls):
        browser.element('[class="button-children"]').click()  # нажатие в "корзину"


    def should_have_text(cls, param):
        browser.element(by.partial_text("Укажите свой адрес")).should(be.visible)  # проверка фразы

    checking = TextChecking()








