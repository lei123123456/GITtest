import sys
import os
sys.path.append(os.getcwd())


import pytest
from base import get_driver
from page.page import PageLog


class TestLogin():
    def setup(self):
        self.driver = PageLog(get_driver.get_driver())

    def teardown(self):
        self.driver.driver.quit()

    @pytest.mark.parametrize("username,pwd,vc",[("13232560056","123456789","8888")])
    def testlogin(self,username,pwd,vc):
        self.driver.page_click_login()
        self.driver.page_input_user(username)
        self.driver.page_input_pwd(pwd)
        self.driver.page_input_vc(vc)
        self.driver.page_click_btn()