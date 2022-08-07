'''数据驱动demo之@pytest.mark.parametrize'''

import pytest
import requests
from jsonschema import validate
import allure
from read_yaml import read_yaml
from read_json import read_json,cmp_dict


class TestApi:
    #最基本的用法
    # @pytest.mark.parametrize('args',["美团","腾讯","阿里","百度"])#参数的值有多少个，那么方法就会执行多少次
    # def test_01_api(self,args):
    #     print(args)

    #解包的用法(ddt,unittest找个框架实现数据驱动的装饰器,@unpack)
    # @pytest.mark.parametrize('args',read_yaml() )
    # def test_01_api(self,args):
    #     '''获得网页新闻的接口'''
    #     url = args['api_request']['url']
    #     method = args['api_request']['method']
    #     headers = args['api_request']['headers']
    #     params = args['api_request']['params']
    #     validate = args["api_validate"]
    #
    #     if method == 'get':
    #         requests.get()
    #     else:
    #         response=requests.post(url,json=params,headers=headers)
    #         for val in validate:
    #            assert val['eq']['code']==response.json()['code']

    @pytest.mark.parametrize('args', read_json())
    @allure.feature("1")
    @allure.story("2")
    @allure.title("用例标题")
    def test_01_api(self, args):
        '''获得网页新闻的接口'''
        url = args['api_request']['url']
        method = args['api_request']['method']
        headers = args['api_request']['headers']
        params = args['api_request']['params']
        eq = args["api_validate"]["eq"]
        try:
            if method == 'get':
                requests.get()
            else:
                response = requests.post(url,json=params,headers=headers)
                # assert code == response.json()["code"]
                # print(response.json())
                cmp_dict(eq,response.json())
        except Exception as e:
            str_error = str(e)
            print(str_error)









