# @File  : read_txt.py
# @Author: yize365
# @Date  :  2020/03/17
# @Function:
# @Remarks:
import os
def read_txt(filename):
    filepath = "../data/" + filename
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8")as f:
            data=f.readlines()
        return data

#测试

#如何解析获取的data,目标格式[(),()]
# def get_data():
#     datas=read_txt('data.txt')
#     arrs = []
#     for line in datas:
#         arr=tuple(line[:-1].split(":"))
#         arrs.append(arr)
#     print(arrs)
#
# get_data()