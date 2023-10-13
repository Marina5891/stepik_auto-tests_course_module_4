from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_book_name()
    page.should_be_book_price()

    page.should_be_message_book_name()
    page.should_be_message_price()

    page.compares_product_name_and_message()
    page.compares_product_price_and_cart_price()
