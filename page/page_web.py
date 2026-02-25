from time import sleep

from selenium.webdriver.common.by import By

from base.base_web import BaseApp

username=By.XPATH,'//*[@name="username"]'
password=By.XPATH,'//*[@name="password"]'
img_verif=By.XPATH,'//*[@placeholder="验证码"]'
login_btu=By.XPATH,'//*[text()="登入系统"]'
web_login_text=By.XPATH,'//cite[text()="超级员工"]'


class PageWebLogin(BaseApp):
    def __page_web_username(self, values):
        sleep(2)
        self.base_input(username,values)

    def __page_web_password(self, values):
        sleep(2)
        self.base_input(password,values)

    # def __page_web_img_verif(self, values):
    #     sleep(2)
    #     self.base_input(img_verif,values)


    def __page_web_login_btu(self):
        sleep(5)
        self.base_click(login_btu)

    def page_web_login_text(self):
        sleep(2)
        return self.base_text(web_login_text)


    def page_web_login(self, name, pwd):
        self.__page_web_username(name)
        self.__page_web_password(pwd)
        # self.__page_web_img_verif(code)
        self.__page_web_login_btu()