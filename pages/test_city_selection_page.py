import allure
from selene import browser, have


class CitySelection:

    def city_selection(self):
      with allure.step('Перейти во вкладку "выбор города"'):
        browser.element('[class="sc-eCstlR fniAzO booklets-widget__city-button"]').click()

    def search(self):
      with allure.step('Ввести в строку поиска название города'):
        browser.element('[class="Input__InputStyled-sc-1kqlv3u-0 kynxqM"]').type('Оренбург')

    def select_element(self):
      with allure.step('Кликнуть по найденному элементу'):
        browser.element('[class="sc-eCstlR fniAzO city-item"]').click()

    def city_check(self):
      with allure.step('Проверить, что установился выбранный город'):
        browser.element('[class="sc-eCstlR fniAzO booklets-widget__city-button"]').should(have.text("Оренбург"))


city = CitySelection()