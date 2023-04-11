import pytest

from PageObjectModel.home_page import HomePage
from TestScript.base_test import BaseTest


class TestHomePage(BaseTest):

    def test_home_page(self):
        home_page = HomePage(self.driver)
        home_page.click_on_manage_cookies_pop_up()
        home_page.mouse_hover_to_vitamins()

