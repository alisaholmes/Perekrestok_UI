import allure
from selene import browser


class Feedback:

    def click_leave_a_review(self):
      with allure.step('нажать на "Оставить отзыв о сайте" снизу'):
        browser.element(
            '[class="sc-eCstlR djqBVS sc-dacGJm dmQoQs"]').click()

    def five_stars(self):
      with allure.step('поставить 5 звезд'):
        browser.element('[for="star5-9"]').click()

    def write_a_review(self):
       with allure.step('написать отзыв'):
        browser.element('[values="[object Object]"]').type("Хорошие продукты!")

    def send(self):
      with allure.step('отправить отзыв'):
        browser.element('[class="sc-eCstlR dzgLvG"]').click()


feedback = Feedback()
