from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    # проверяет на корректный url адрес корзины
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket url not found"

    # проверяет, что корзина пуста
    def should_be_basket_is_empty(self):
        assert not self.is_element_present(
            *BasketPageLocators.BASKET_FORM), "Basket isn't empty"

    # проверяет, что есть сообщение на странице
    def should_be_message_on_basket_page(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_MESSAGE), "Message on basket page is not presented, but should be"

    # проверяет текст сообщения о том, что корзина пуста
    def should_be_message_about_empty_basket(self):
        message = self.browser.find_element(
            *BasketPageLocators.BASKET_MESSAGE).text
        assert "Your basket is empty." in message, "Message on page is not about empty basket"

    # проверяет наличие сообщения о том, что корзина пуста, хотя такого сообщения быть не должно
    def should_not_be_message_about_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            "Message about an empty basket is presented, but should not be"
