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

    # проверяет, что на странице есть сообщение о том, что корзина пуста
    def should_be_message_on_basket_page(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_MESSAGE), "Message on basket page is not presented, but should be"
