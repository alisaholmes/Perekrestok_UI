from selene import browser


class Feedback:

    def click_leave_a_review(self):
        browser.element(
            '[class="sc-eCstlR djqBVS sc-dacGJm dmQoQs"]').click()  # нажать на "Оставить отзыв о сайте" справа

    def five_stars(self):
        browser.element('[for="star5-9"]').click()  # поставить 5 звезд

    def write_a_review(self):
        browser.element('[values="[object Object]"]').type("Хорошие продукты!")  # написать отзыв

    def send(self):
        browser.element('[class="sc-eCstlR dzgLvG"]').click()  # отправить отзыв


feedback = Feedback()
