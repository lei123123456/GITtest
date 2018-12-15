import page
from base.base import Base


class PageLog(Base):

    def page_click_login(self):
        self.base_click(page.loc_log)

    def page_click_btn(self):
        self.base_click(page.loc_btn)

    def page_input_user(self,name):
        self.base_input(page.loc_name,name)

    def page_input_pwd(self,pwd):
        self.base_input(page.loc_pwd,pwd)

    def page_input_vc(self,vc):
        self.base_input(page.loc_vc,vc)