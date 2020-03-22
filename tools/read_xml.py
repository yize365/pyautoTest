# @File  : ReadXml.py
# @Author: yize365
# @Date  :  2019/12/21
# @Function:
# @Remarks:

from xml.dom import minidom
# class readXml():
#     def read_xml(self):
#         root=minidom.parse("../DataXml/data.xml")
#         firstnode=root.getElementsByTagName('jia')[0]
#         secondnode=firstnode.getElementsByTagName("num1")[0].firstChild.data
#         return secondnode
class Read_Xml():
    def read_xml(self,file_path,firstnode,twonode):
        root=minidom.parse(file_path)
        firstnode=root.getElementsByTagName(firstnode)[0]
        secondnode=firstnode.getElementsByTagName(twonode)[0].firstChild.data
        return secondnode
# read_xml_data=readXml()
# print(read_xml_data.read_xml())