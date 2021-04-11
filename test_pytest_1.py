import pytest
import allure

class TestSample(object):
    @allure.feature('test_module_模块')
    @allure.story('test_story_1_故事')
    @allure.severity('blocker严重等级')
    def test_equal(self):
        """testcase1"""
        assert 1==1

    @allure.feature('test_module_2')
    @allure.story('test_story_2')
    @allure.severity('normal')
    def test_not_equal(self):
        """testcase2"""
        assert 1!=0
