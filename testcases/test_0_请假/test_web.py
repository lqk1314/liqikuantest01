import pytest

from base import log
from common.yaml_util import read_yaml




class TestWebLogin:

    @pytest.mark.parametrize("key,values,values1",read_yaml('testcases/test_0_请假/test_web.yaml',"web_day"))
    def test_day_off(self,web_login, pages, key,values, values1):
        try:
            (pages["qingjia"].page_web_qingjia(values,values1))

        except Exception as e:
            log.error("错误原因：",e)
            raise