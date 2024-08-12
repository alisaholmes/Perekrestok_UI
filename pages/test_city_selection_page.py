from selene import browser, have


class CitySelection:

    def city_selection(self):
        browser.element('[class="sc-eCstlR fniAzO booklets-widget__city-button"]').click()  #переход во вкладку выбор города

    def search(self):
        browser.element('[class="Input__InputStyled-sc-1kqlv3u-0 kynxqM"]').type('Оренбург')  #ввод в строку поиска

    def select_element(self):
        browser.element('[class="sc-eCstlR fniAzO city-item"]').click()  #клик по найденному элементу

    def city_check(self):
        browser.element('[class="sc-eCstlR fniAzO booklets-widget__city-button"]').should(have.text("Оренбург"))


city = CitySelection()