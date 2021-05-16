import json

def read_json():
    '''读取单个json文件'''
    with open(r'TestData/get_new_json.json',encoding='utf-8') as f:
        data = json.load(f)
        return data

#对比俩个json属于包含关系
def cmp_dict(src_data,dst_data):
    assert type(src_data) == type(dst_data),"type: '{}' != '{}'".format(type(src_data), type(dst_data))
    if isinstance(src_data,dict):
        for key in src_data:
            # assert dst_data.has_key(key)
            cmp_dict(src_data[key],dst_data[key])
    elif isinstance(src_data,list):
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            cmp_dict(src_list, dst_list)
    else:
        assert src_data == dst_data,"value '{}' != '{}'".format(src_data, dst_data)

#对比两个json属于相等关系
def cmp_dict2(src_data,dst_data):
    assert type(src_data) == type(dst_data),"type: '{}' != '{}'".format(type(src_data), type(dst_data))
    if isinstance(src_data,dict):
        assert len(src_data) == len(dst_data),"dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for key in src_data:
            assert dst_data.has_key(key)
            cmp_dict(src_data[key],dst_data[key])
    elif isinstance(src_data,list):
        assert len(src_data) == len(dst_data),"list len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            cmp_dict(src_list, dst_list)
    else:
        assert src_data == dst_data,"value '{}' != '{}'".format(src_data, dst_data)


if __name__ == "__main__":
    # print(read_json())
    xx = {"111": None, "23456": {"22222": 999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    cmp_dict(yy,xx)