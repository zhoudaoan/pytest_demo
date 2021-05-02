

import yaml

def read_yaml():
    '''
    读取单个yaml文件
    '''
    with open('TestData/get_new.yaml',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data

if __name__ == "__main__":
    print(read_yaml())