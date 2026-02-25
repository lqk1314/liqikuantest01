#
# 封装页面所有公共方法
import os

from time import strftime

from selenium.webdriver.support.wait import WebDriverWait

from base import log


class BaseApp:
    #初始化
    def __init__(self, driver):
        self.driver=driver

    #定位元素，显式等待
    def base_find(self, loc):
        log.info("正在调用查找元素：".format(loc))
        return WebDriverWait(self.driver,20,0.5).until(lambda x:x.find_element(*loc))

    #输入方法
    def base_input(self, loc, values):
        log.info("正在调用输入查找元素：{}，正在输入内容：{}".format(loc,values))
        e1=self.base_find(loc)
        e1.clear()
        e1.send_keys(values)

    #点击
    def base_click(self, loc):
        log.info("正在调用点击方法：{}".format(loc))
        self.base_find(loc).click()

    #获取文本
    def base_text(self, loc):
        log.info("正在调用获取文本：{}".format(loc))
        return self.base_find(loc).text

    #截图
    def base_screenshot(self):
        log.info("正在调用截图")
        self.driver.get_screenshot_as_file(os.path.join('log', 'log_web.py')+os.sep+'log_app_{}.png'.format(strftime('%Y%m%d_%H%M%S')))

    #滚动
    def base_roll(self):
        print('滚动')
        js_down="window.scrollTo(0,10000);"
        self.driver.execute_script(js_down)

    def base_roll1(self):
        print('滚动')
        js_lift="window.scrollTo(10000,0);"
        self.driver.execute_script(js_lift)

    #切换页面
    def base_switch_pages(self, loc):
        e1=self.base_find(loc)
        self.driver.switch_to.frame(e1)

    def base_switch_pages2(self):
        self.driver.switch_to.default_content()



