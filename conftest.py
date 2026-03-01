import pytest
from selenium import webdriver

from base import log
from page.page_chuchai import PageWebchuchai
from page.page_day import PageWebqingjia
from page.page_web import PageWebLogin



@pytest.fixture(scope='session')
def driver():
        driver=webdriver.Edge()
        driver.get('http://oa.project.hctestedu.com/home/login/index.html')
        driver.maximize_window()
        yield driver
        driver.quit()
@pytest.fixture(scope='session')
def login_page(driver):
    return PageWebLogin(driver)

@pytest.fixture(scope='session')
def web_login(login_page):
    try:
        (login_page.page_web_login('admin','admin123'))
        yield login_page
    except Exception as e:
        log.error(f"错误原因：{e}")
        raise

@pytest.fixture(scope='function')
def pages(driver):
    qingjia=PageWebqingjia(driver)
    chuchuai=PageWebchuchai(driver)
    return {
        "qingjia":qingjia,
        "chuchai":chuchuai
    }




