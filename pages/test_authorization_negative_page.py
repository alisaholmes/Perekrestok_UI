import allure
from selene import browser, be, by


class AuthorizationNegative:

    def tap(self):
      with allure.step('Нажать по иконке пользователя в правом верхнем углу'):
        browser.element('[class="Flex-brknwi-0 edwWgR"]').click()

    def authorization(self, number):
      with allure.step('Нажать кнопку "Войти" и ввести ложный номер'):
        browser.element('[class="sc-eCstlR gPywZE login-x5__button primary"]').click()
        browser.element("#username").type(number)

    def should_have_text(self, text):
      with allure.step('Проверить текст сообщения об ошибке'):
        browser.element(by.partial_text(text)).should(be.visible)




authorization_negative = AuthorizationNegative()

