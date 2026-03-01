import pytest

from page.page_chuchai import PageWebchuchai



class TestChuchai:
    def test_chuchai(self,web_login,pages):
        try:
            pages['chuchai'].page_chuchai()

        except Exception as e:
            print(f'错误原因：{e}')
            raise
