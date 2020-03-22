# @File  : read_yaml.py.py
# @Author: yize365
# @Date  :  2020/02/28
# @Function:
# @Remarks:
import yaml
def read_yaml(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8")as f:
        return yaml.load(f)

"""
#解析方法举例，其他文件调用(注意yaml文件中的格式使用时空格)
def get_data():
    datas = read_yaml("login.yaml")
    arrs = []
    for data in datas["Login_Data"].values():
        arrs.append((data['username'], data['pwd'], data['code'],data['expect_result'],data['testtype']))
    return arrs

#打印输出(列表嵌套元祖)
print(get_data())
"""