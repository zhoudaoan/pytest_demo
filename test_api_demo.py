#数据驱动demo

import pytest

class TestApi:

    @pytest.mark.parametrize('args',["美团","腾讯","阿里","百度"])
    def test_01_api(self,args):
        print(args)







