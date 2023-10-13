from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRICE = (
        By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    PRICE_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")
