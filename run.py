import pytest
import os

if __name__ == '__main__':
    pytest.main(["-sq", "--clean-alluredir", "./allure-results"])
    os.system("allure generate ./allure-results/ -o ./allure-report/ --clean")