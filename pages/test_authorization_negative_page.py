from selene import browser, be, by


class AuthorizationNegative:

    def tap(self):
        browser.element('[class="Flex-brknwi-0 edwWgR"]').click()  # нажатие по иконке пользователя в правом верхнем углу

    def authorization(self, number):
        browser.element('[class="sc-eCstlR gPywZE login-x5__button primary"]').click()  # тап по кнопке "Войти"
        browser.element("#username").type(number)  # ввод ложного номера

    def should_have_text(self, text):
        browser.element(by.partial_text(text)).should(be.visible)  # проверка текста сообщения об ошибке




authorization_negative = AuthorizationNegative()

