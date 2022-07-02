import json


def read_json():
    '''读取单个json文件'''
    with open(r'TestData/get_new_json.json', encoding='utf-8') as f:
        data = json.load(f)
        return data


# 对比俩个json属于包含关系
def cmp_dict(src_data, dst_data):
    assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
    if isinstance(src_data, dict):
        for key in src_data:
            # assert dst_data.has_key(key)
            cmp_dict(src_data[key], dst_data[key])
    elif isinstance(src_data, list):
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            cmp_dict(src_list, dst_list)
    else:
        assert src_data == dst_data, "value '{}' != '{}'".format(src_data, dst_data)


# 对比两个json属于相等关系
def cmp_dict2(src_data, dst_data):
    assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
    if isinstance(src_data, dict):
        assert len(src_data) == len(dst_data), "dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for key in src_data:
            # assert dst_data.has_key(key)
            assert dst_data
            cmp_dict(src_data[key], dst_data[key])
    elif isinstance(src_data, list):
        assert len(src_data) == len(dst_data), "list len: '{}' != '{}'".format(len(src_data), len(dst_data))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            cmp_dict(src_list, dst_list)
    else:
        assert src_data == dst_data, "value '{}' != '{}'".format(src_data, dst_data)


# 对比两个json
def cmp(src_data, dst_data):
    if isinstance(src_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                raise Exception("src_data与dst_data不相同的key："+key)
        for key in src_data:
            if key in dst_data:
                thiskey = key
                """递归"""
                cmp(src_data[key], dst_data[key])
            else:
                dst_data[key] = ["dst不存在这个key"+key]

    elif isinstance(src_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data):
            print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            """递归"""
            cmp(src_list, dst_list)
    else:
        if str(src_data) != str(dst_data):
            raise Exception("src_data与dst_data不相同的value值是："+str(src_data))


if __name__ == "__main__":
    # print(read_json())
    xx = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["11", "3333", "4444"]}}
    cmp(yy, xx)
