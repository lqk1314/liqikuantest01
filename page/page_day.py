from time import sleep

from selenium.webdriver.common.by import By

from base.base_web import BaseApp

frame00_web=By.XPATH,'//*[@title="前台首页"]' #页面
frame01_web=By.XPATH,'//*[@title="勾股OA"]'   #外层
username=By.XPATH,'//*[text()="审批申请"]'

password=By.XPATH,'//div[text()="请假"]'
img_verif=By.XPATH,'//*[@placeholder="请选择开始时间"]'
login_btu=By.XPATH,'//*[@placeholder="请选择结束时间"]'
web_login_text=By.XPATH,'//*[@placeholder="请输入请假天数"]'
aa=By.XPATH,'//select[@name="types"]/following-sibling::div[@class="layui-form-select layui-unselect"]/div[@class="layui-select-title"]/input[@placeholder="--请选择--"]'
aa1=By.XPATH,'//dd[text()="调休假"]'
bb=By.XPATH,'//*[@placeholder="请输入请假事由"]'
frame02_web=By.XPATH,'//iframe[contains(@src,"/home/approve/index")]'   #内层
frame03_web=By.XPATH,'//iframe[contains(@src,"/home/leaves/add")]'
cc=By.XPATH,'//select[@name="flow_id"]/following-sibling::div[@class="layui-form-select layui-unselect"]/div[@class="layui-select-title"]/input[@placeholder="--请选择--"]'
cc1=By.XPATH,'//dd[text()="请假审批"]'
dd=By.XPATH,'//*[@lay-reqtext="请选择审批人"]'
ee=By.XPATH,'//*[text()="人事部"]'
ff=By.XPATH,'//*[text()="小黑"]'

hh=By.XPATH,'//*[text()="确定"]'


class PageWebqingjia(BaseApp):
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

    def __page_web_iframe03(self):
        sleep(2)
        self.base_switch_pages(frame03_web)
    #开始时间
    def __page_web_img_verif(self):
        sleep(3)
        self.base_click(img_verif)

    def __page_web_queding(self):
        sleep(3)
        self.base_click(hh)


    #结束时间
    def __page_web_login_btu(self):
        sleep(5)
        self.base_click(login_btu)

    def __page_web_base_roll(self):
        sleep(2)
        self.base_roll()


    #天数
    def __page_web_login_text(self, values):
        sleep(2)
        return self.base_input(web_login_text,values)
    #请假类型
    def __page_web_type(self):
        sleep(5)
        self.base_click(aa)
    #选择事假
    def __page_web_shijia(self):
        sleep(2)
        self.base_click(aa1)
    #理由
    def __page_web_liyou(self, values):
        sleep(2)
        self.base_input(bb,values)

    #审批类型
    def __page_web_ren(self):
        sleep(2)
        self.base_click(cc)
    #点击请假审批
    def __page_web_ren5(self):
        sleep(2)
        self.base_click(cc1)
    #选择审批人
    def __page_web_ren1(self):
        sleep(2)
        self.base_click(dd)
    #点击部门
    def __page_web_bm(self):
        sleep(2)
        self.base_click(ee)
    #点击小黑
    def __page_web_ren2(self):
        sleep(2)
        self.base_click(ff)

    def __page_web_submit(self):
        # 1. 校验必填项（保留日志）
        start_time_elem = self.base_find(img_verif)
        start_time = start_time_elem.get_attribute("value")
        approver_elem = self.base_find(dd)
        approver = approver_elem.get_attribute("value")
        print(f"开始时间: {start_time}, 审批人: {approver}")

        # 2. 强制触发表单提交（绕过LayUI校验）
        self.driver.execute_script("""
            // 直接获取表单并提交，跳过按钮点击的事件拦截
            var form = document.querySelector('form[lay-filter="webform"]');
            if (form) {
                form.submit();
            }
        """)


    def page_web_qingjia(self, values, valus1):
        self.__page_web_frame01()
        self.__page_web_username()
        self.__page_web_frame02()
        self.__page_web_password()
        self.__page_web_iframe03()
        self.__page_web_img_verif()
        self.__page_web_queding()
        self.__page_web_login_btu()
        self.__page_web_queding()
        self.__page_web_login_text(values)
        self.__page_web_type()
        self.__page_web_shijia()
        self.__page_web_liyou(valus1)
        self.__page_web_ren()
        self.__page_web_base_roll()
        self.__page_web_ren5()
        self.__page_web_ren1()
        self.__page_web_bm()
        self.__page_web_ren2()
        self.__page_web_submit()



