# @File  : read_json.py
# @Author: yize365
# @Date  :  2020/02/22
# @Function:
# @Remarks:
import json
#从json文件读取json格式的数据
def read_json(filename):
    filepath="../data/"+filename
    with open(filepath, "r", encoding="utf-8")as f:
        return json.load(f)

#使用json.dumps()将python数据(字典格式)转化为Json数据(str),然后将json数据写入到文件
#注意此方法data为python数据格式
def write_json(filename,data):
    filepath = "../data/" + filename
    with open(filepath, "w", encoding="utf-8")as f:
        f.write(json.dumps(data))

#注意此方法data为json格式
def write_jsondata_to_jsonfile(filename, data):
    filepath = "../data/" + filename
    with open(filepath, "w", encoding="utf-8")as f:
        json.dump(data, f)


#json数据
# json_str='{"id":1,"name":"xiaoming"}'
#将json数据转换为python数据(字典类型)
# print(type(json.loads(json_str)))

#python数据
# python_data={'id':1,'name':'xiaoming','sex':'man'}
#python数据转化为json数据
# json.dumps(python_data)
# write_jsondata_to_jsonfile('1234567.json',json_str)


#解析方法举例，其他文件调用,根据用例需要的参数进行改造
# def get_data():
    # datas = read_json("login.json")
    # arrs = []
    # for data in datas.values():
    #     arrs.append((data['username'], data['pwd'], data['code'],data['expect_result'],data['testtype']))
    # return arrs
#打印输出(列表嵌套元祖)
# print(get_data())
