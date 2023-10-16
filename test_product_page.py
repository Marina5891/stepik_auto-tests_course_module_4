import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_message_on_basket_page()
    basket_page.should_be_message_about_empty_basket()

# гость должен увидеть ссылку для входа на странице продукта


def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()

# гость может перейти на страницу авторизации со страницы продукта


def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# проверяет, что пользователь может добавить товар в корзину


# @pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
# def test_guest_can_add_product_to_basket(browser, number):
#     url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
#     page = ProductPage(browser, url)
#     page.open()
#     page.should_be_basket_button()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()

#     page.should_be_book_name()
#     page.should_be_book_price()

#     page.should_be_message_with_book_name()
#     page.should_be_message_with_price()

#     page.compares_product_name_and_message()
#     page.compares_product_price_and_cart_price()

@pytest.mark.xfail
# проверяет, что пользователь не видит сообщения об успешном добавлении товара после его добавления в корзину
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.should_not_be_success_message()

# проверяет, что при открытии страницы пользователь не видит сообщения об успешном добавлении товара в корзину


def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
# проверяет, что сообщение об успешном добавлении товара в корзину исчезает спустя некоторое время
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_is_disappeared()
