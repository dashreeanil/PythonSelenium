from selenium.webdriver.common.by import By
from GenericUtil import random_utility,global_variables

from PageObjectModel.base_page import BasePage


class CreateAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    password = random_utility.password_generator(10)
    first_name = (By.XPATH, "//input[@id='firstName']")
    last_name = (By.XPATH, "//input[@id='lastName']")
    email_address = (By.XPATH, "//input[@id='email']")
    create_a_password = (By.XPATH, "//input[@id='password']")
    confirm_password = (By.XPATH, "//input[@id='confirmPassword']")
    not_today = (By.XPATH, "//label[@for='optOut']//span[@class='jsx-b76e2c7fc84de7d9 radio-input']")
    email = (By.XPATH, "//fieldset[@class='MarketingPreferences_checkboxGroupWrapper__q1ugb']//label[1]")
    sms = (By.XPATH, "//label[normalize-space()='SMS']")
    i_agree_to_the_rewards_for_life = (By.XPATH, "//label[@class='TermsAndConditions_label__dbZUA']")
    create_an_account = (By.XPATH, "//button[normalize-space()='Create an account']")
    sign_in = (By.XPATH, "//a[@class='jsx-507bb6a5283c3c9e ghost block signup_link']")
    i_signed_up_in_store = (By.XPATH, "//label[@for='alreadyJoined']//span[@class='jsx-b76e2c7fc84de7d9 radio-input']")

    def enter_first_name(self):
        first_name = random_utility.get_random_name(7)
        self.send_keys(*self.first_name, value=first_name)

    def enter_last_name(self):
        last_name = random_utility.get_random_name(5)
        self.send_keys(*self.last_name, value=last_name)

    def enter_email_address(self):
        email_id = random_utility.email_generator()
        self.send_keys(*self.email_address, value=email_id)

    def enter_password(self):
        self.send_keys(*self.create_a_password, value=global_variables.password)

    def confirm_password(self):
        self.waitForElement(*self.confirm_password)
        self.send_keys(*self.confirm_password, value=global_variables.password)

    def click_on_not_today_option(self):
        self.click(*self.not_today)

    def click_on_email_sms_check_box(self):
        self.check_checkbox(*self.email)
        self.check_checkbox(*self.sms)

    def check_i_agree_to_the_rewards_for_life(self):
        self.check_checkbox(*self.i_agree_to_the_rewards_for_life)

    def click_on_sign_in_button(self):
        self.click(*self.sign_in)

    def enter_first_name_user_define_data(self,data):
        first_name = random_utility.get_random_name(7)
        self.send_keys(*self.first_name, value=data)

    def enter_last_name_user_define_data(self,data):
        last_name = random_utility.get_random_name(5)
        self.send_keys(*self.last_name, value=data)

    def enter_email_address_user_define_data(self,data):
        email_id = random_utility.email_generator()
        self.send_keys(*self.email_address, value=data)


    def fill_account_creation_form(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_email_address()
        self.enter_password()
        self.confirm_password
        self.click_on_not_today_option()
        self.click_on_email_sms_check_box()
        self.check_i_agree_to_the_rewards_for_life()
        self.click_on_sign_in_button()

    def fill_account_creation_form_user_define_data(self,data):
        self.enter_first_name_user_define_data(data["first_name"])
        self.enter_last_name_user_define_data(data["last_name"])
        self.enter_email_address_user_define_data(data["email_id"])
        self.enter_password()
        self.confirm_password
        self.click_on_not_today_option()
        self.click_on_email_sms_check_box()
        self.check_i_agree_to_the_rewards_for_life()
        self.click_on_sign_in_button()
