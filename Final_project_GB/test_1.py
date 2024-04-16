import time
import yaml
from testpage import OperationsHelper

with open('./datatest.yaml') as f:
    data = yaml.safe_load(f)


def test_login_and_about(browser):
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(data['username'])
    test_page.enter_pass(data['password'])
    test_page.click_login_button()
    time.sleep(5)
    assert test_page.get_username_label() == f'Hello, secondone'
    test_page.click_about()
    time.sleep(5)
    assert test_page.get_about_header() == f'About Page'
    assert test_page.get_about_css_property() == '32px', "Font size is not 32px"
