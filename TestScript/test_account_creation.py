import pytest

from PageObjectModel.create_account_page import CreateAccountPage
from PageObjectModel.home_page import HomePage
from TestScript.base_test import BaseTest


class TestAccountCreation(BaseTest):

    def test_create_account(self):
        home_page = HomePage(self.driver)
        home_page.click_on_manage_cookies_pop_up()
        home_page.click_on_rewards()
        create_account_page = CreateAccountPage(self.driver)
        create_account_page.fill_account_creation_form()

    def test_create_account_using_user_defined_data(self, get_data):
        home_page = HomePage(self.driver)
        home_page.click_on_manage_cookies_pop_up()
        home_page.click_on_rewards()
        create_account_page = CreateAccountPage(self.driver)
        create_account_page.fill_account_creation_form_user_define_data(get_data)

    @pytest.fixture(params=[{"first_name": "dashree", "last_name": "anil", "email_id": "abcdzyx@gmail.com"},
                            {"first_name": "kumar", "last_name": "dashree", "email_id": "zyxdcba@gmail.com"}])
    def get_data(self, request):
        return request.param
