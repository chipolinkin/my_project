from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    BOOK_NAME1 = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME2 = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    BASKET_PRICE1 = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    BASKET_PRICE2 = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    
    
