from selenium.webdriver.common.by import By

from PageObjectModel.base_page import BasePage
from PageObjectModel.create_account_page import CreateAccountPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver



    manage_cookies = (By.XPATH, "//div/button[.='Manage cookies']")
    yes_i_accept = (By.XPATH, "//button[.='Yes I accept']")
    vitamin_and_supplement = (By.XPATH, "//a[@class='Desktop-module--link--49cdf'][normalize-space()='Vitamins & Supplements']")
    food_drink = (By.XPATH, "//a[@class='Desktop-module--link--49cdf'][normalize-space()='Food & Drink']")
    sports_nutrition = (By.XPATH, "//a[@class='Desktop-module--link--49cdf'][normalize-space()='Sports Nutrition']")
    beauty = (By.XPATH, "//a[normalize-space()='Beauty']")
    weight_management = (By.XPATH, "//a[@class='Desktop-module--link--49cdf'][normalize-space()='Weight Management']")
    offers = (By.XPATH, "//a[normalize-space()='Offers']")
    wellness_needs = (By.XPATH, "//a[normalize-space()='Wellness Needs']")
    outlet = (By.XPATH, "//a[@class='Desktop-module--link--49cdf'][normalize-space()='Outlet']")
    the_health_hub = (By.XPATH, "//a[normalize-space()='The Health Hub']")
    account = (By.CSS_SELECTOR,"div[class='Desktop-module--men")
    stores  = (By.XPATH,"//section[@data-hydration-on-demand='true']//div[@data")
    rewards = (By.XPATH,"//div[@class='Desktop-module--menu--0bfa6']//div//div[@id='data-cs-mask-rewards']//a[@class='MenuItem-module--button--fa69a']")
    help = (By.XPATH, "//section[@data-hydration-on-demand='true']//div[@data-menuitem-type='help']//a")
    basket = (By.XPATH, "//div[@class='Desktop-module--menu--0bfa6']//div//div[@id='data-cs-mask-basket']//a[@class='MenuItem-module--button--fa69a']")

    def click_on_manage_cookies_pop_up(self):
        if self.check_if_element_exits(*self.manage_cookies):
            self.click(*self.yes_i_accept)

    def mouse_hover_to_vitamins(self):
        self.move_to_element(*self.vitamin_and_supplement)

    def click_on_rewards(self):
        self.click(*self.rewards)

