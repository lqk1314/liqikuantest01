import pytest
from selenium import webdriver

from base import log
from base.base_web import BaseApp
from common.yaml_util import read_yaml
from page.page_day import PageWebqingjia
from page.page_web import PageWebLogin

@pytest.fixture(scope='class')
def driver():
        driver=webdriver.Edge()
        driver.get('http://oa.project.hctestedu.com/home/login/index.html')
        driver.maximize_window()
        yield driver
        driver.quit()

@pytest.fixture(scope='function')
def pages(driver):
        login_page=PageWebLogin(driver)
        jietu_page=BaseApp(driver)
        qingjia_page=PageWebqingjia(driver)
        return {
            "login":login_page,
            "jirtu":jietu_page,
            "qingjia_page":qingjia_page
        }

class Test_web_login:


    @pytest.mark.parametrize("key,name,pwd,expect_text",read_yaml('testcases/test_web.yaml',"web_log"))
    def test_web_login(self, pages,key,name,pwd,expect_text):
        try:
            (pages["login"].page_web_login(name,pwd))
            text=pages['login'].page_web_login_text()
            assert expect_text==text
        except Exception as e:
            log.error("错误原因：",e)
            raise

    @pytest.mark.parametrize("key,values,values1",read_yaml('testcases/test_web.yaml',"web_day"))
    def test_day_off(self, pages, key,values, values1):
        try:
            (pages["qingjia_page"].page_web_qingjia(values,values1))
        except Exception as e:
            log.error("错误原因：",e)
            raise