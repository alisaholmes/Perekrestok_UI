import allure
from allure_commons.types import Severity
from selene import browser, be, by

from pages.test_authorization_negative_page import authorization_negative
from pages.test_choosing_delivery_address_page import delivery_address
from pages.test_city_selection_page import city
from pages.test_empty_cart_page import cart
from pages.test_feedback_page import feedback
from pages.test_text_checking_page import text_checking
from pages.test_clear_to_cart_page import clear_cart


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Корзина")
@allure.story("Проверка выбора товара")
def test_text_checking():
    text_checking.open()
    text_checking.sales_go_to_section()
    text_checking.product_card()
    text_checking.add_to_cart()
    text_checking.should_have_text()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Авторизация")
@allure.story("Авторизация с неверным номером телефона")
def test_authorization_negative():
    text_checking.open()
    authorization_negative.tap()
    authorization_negative.authorization("70000000000")
    authorization_negative.should_have_text("Неверный формат номера")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Корзина")
@allure.story("Проверка пустой корзины")
def test_empty_cart():
    text_checking.open()
    cart.go_to_cart()
    cart.empty_cart()
    cart.start_shopping()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Отзыв")
@allure.story("Проверка формы отправки отзыва")
def test_feedback():
    text_checking.open()
    feedback.click_leave_a_review()
    feedback.five_stars()
    feedback.write_a_review()
    feedback.send()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Адрес доставки")
@allure.story("Выбор города")
def test_city_selection():
    text_checking.open()
    city.city_selection()
    city.search()
    city.select_element()
    city.city_check()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Адрес доставки")
@allure.story("Выбор адреса доставки")
def test_choosing_delivery_address():
    text_checking.open()
    delivery_address.ready_meals()
    delivery_address.add_product()
    delivery_address.check_text()
    delivery_address.list_of_addresses()
    delivery_address.address_selection()
    delivery_address.confirmation()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alisaholmes")
@allure.feature("Корзина")
@allure.story("Очистка корзины")
def test_clear_to_cart():
    text_checking.open()
    delivery_address.ready_meals()
    delivery_address.add_product()
    delivery_address.check_text()
    delivery_address.list_of_addresses()
    delivery_address.address_selection()
    delivery_address.confirmation()
    clear_cart.add_product()
    clear_cart.go_to_shopping_cart()
    clear_cart.checking_product_availability()
    clear_cart.clear_button()






