from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Добавляет товар в корзину
    def add_product_to_basket(self):
        add_basket_button = self.browser.find_element(
            *ProductPageLocators.BASKET_BUTTON)
        add_basket_button.click()

     # Сравнивает название книги с названием в сообщении
    def compares_product_name_and_message(self):
        success_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE).text
        book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text
        assert book_name == success_message, "The title of the book does not match the title in the message"

    # Сравнивает цену книги с ценой в сообщении
    def compares_product_price_and_cart_price(self):
        price_message = self.browser.find_element(
            *ProductPageLocators.PRICE_MESSAGE).text
        price = self.browser.find_element(
            *ProductPageLocators.PRICE).text
        assert price == price_message, "The price of the product does not match the price in the message"

    # Проверяет наличие кнопки на странице
    def should_be_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    # Проверяет наличие названия у книги, добавляемой в корзину
    def should_be_book_name(self):
        assert self.is_element_present(
            *ProductPageLocators.BOOK_NAME), "Book name not found"

    # Проверяет наличие цены у книги, добавляемой в корзину
    def should_be_book_price(self):
        assert self.is_element_present(
            *ProductPageLocators.PRICE), "Price not found"

    # Проверяет наличие сообщения об успешном добавлении книги в корзину
    def should_be_message_with_book_name(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Message with book name not found"

    # Проверяет наличие сообщения с ценой книги
    def should_be_message_with_price(self):
        assert self.is_element_present(
            *ProductPageLocators.PRICE_MESSAGE), "Message with price not found"

    # Проверяет отсутствие сообщения об успешном добавлении книги в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # Проверяет, что сообщение об успешном добавлении книги в корзину
    # со временем пропадает со страницы
    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
