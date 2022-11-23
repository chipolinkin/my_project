from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def right_name(self):
        name1 = self.browser.find_element(*ProductPageLocators.BOOK_NAME1).text
        name2 = self.browser.find_element(*ProductPageLocators.BOOK_NAME2).text
        assert name1 == name2

    def right_price(self):
        price1 = self.browser.find_element(*ProductPageLocators.BASKET_PRICE1).text
        price2 = self.browser.find_element(*ProductPageLocators.BASKET_PRICE2).text
        assert price1 == price2






