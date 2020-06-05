# import pytest
# from appium import webdriver
# from selenium.webdriver.common.by import By
# from Base.base import Base
#
#
# class TestSearch:
#
#     def setup_class(self):
#         """声明driver"""
#         # server 启动参数
#         desired_caps = {
#             'platformName': "Android",
#             'platformVersion': '5.1',
#             'deviceName': 'sanxing',
#             'appPackage': 'com.android.settings',
#             'appActivity': '.Settings'
#         }
#         # 声明手机驱动对象
#         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
#         # 实例化Base类
#         self.base_obj = Base(self.driver)
#
#         """页面元素"""
#         # 搜索按钮
#         self.search_btn = (By.ID, "com.android.settings:id/search")
#         # 输入框
#         self.search_input = (By.ID, "android:id/search_src_text")
#         # 搜索结果
#         self.search_result = (By.ID, "com.android.settings:id/title")
#
#     def teardown_class(self):
#         """退出driver"""
#         self.driver.quit()
#
#     @pytest.fixture(scope="class", autouse=True)  # 因为只点击一次搜索按钮 自动运行
#     def click_search_btn(self):
#         """点击搜索按钮 1次 输入之前运行"""
#         # 点击搜索
#         self.base_obj.click_ele(self.search_btn)
#
#     @pytest.mark.parametrize("search_text,search_result", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
#     def test_search(self, search_text, search_result):
#         """内容输入 和 结果断言"""
#         # 输入框
#         self.base_obj.send_ele(self.search_input, search_text)
#
#         # 搜索结果
#         results = self.base_obj.search_eles(self.search_result)
#         # 断言 -列表式断言
#         assert search_result in [i.text for i in results]
import pytest
from appium import webdriver

from Page.searchPage import SearchPage


class TestSearch:

    def setup_class(self):
        """声明driver"""
        # server 启动参数
        desired_caps = {
            'platformName': "Android",
            'platformVersion': '5.1',
            'deviceName': 'sanxing',
            'appPackage': 'com.android.settings',
            'appActivity': '.Settings'
        }
        # 声明手机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        # 实例化页面类
        self.sp_obj = SearchPage(self.driver)

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)  # 因为只点击一次搜索按钮 自动运行
    def click_search_btn(self):
        """点击搜索按钮 1次 输入之前运行"""
        # 点击搜索
        self.sp_obj.click_search_btn()

    @pytest.mark.parametrize("search_text,search_result", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search(self, search_text, search_result):
        """内容输入 和 结果断言"""
        # 输入框
        self.sp_obj.send_search_text(search_text)

        # 断言 -列表式断言
        assert search_result in self.sp_obj.get_search_result()
