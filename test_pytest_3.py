import pytest



@pytest.fixture()  # 用例的调用
def init():
    print('init....')
    return 2


data = [123, 456]


@pytest.mark.do  # 运行指定的case
@pytest.mark.parametrize("pwd", data)  # 参数化
def test1(init, pwd):
    print(pwd)


@pytest.mark.undo
def test2(init):
    print("test2")


