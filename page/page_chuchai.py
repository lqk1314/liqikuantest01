from time import sleep

from selenium.webdriver.common.by import By

from base.base_web import BaseApp

frame00_web=By.XPATH,'//*[@title="前台首页"]' #页面
frame01_web=By.XPATH,'//*[@title="勾股OA"]'   #外层
username=By.XPATH,'//*[text()="审批申请"]'
password=By.XPATH,'//div[text()="出差"]'
frame02_web=By.XPATH,'//iframe[contains(@src,"/home/approve/index")]'   #内层




class PageWebchuchai(BaseApp):
    #切换页面
    def __page_web_frame01(self):
        sleep(2)
        self.base_switch_pages(frame01_web)
    #点击审批申请
    def __page_web_username(self,):
        sleep(2)
        self.base_click(username)
    #切换页面
    # def __page_web_frame00(self):
    #     sleep(2)
    #     self.base_switch_pages(frame00_web)
    #切换页面
    def __page_web_frame02(self):
        sleep(2)
        self.base_switch_pages(frame02_web)

    # 点击请假
    def __page_web_password(self):
        sleep(2)
        self.base_click(password)

    def page_chuchai(self):
        self.__page_web_frame01()
        self.__page_web_username()
        self.__page_web_frame02()
        self.__page_web_password()