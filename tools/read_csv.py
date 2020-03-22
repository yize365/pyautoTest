# @File  : ReadCsv.py
# @Author: yize365
# @Date  :  2019/12/21
# @Function:
# @Remarks:
import csv
class Read_Csv():
    def read_csv(self):
        ret_list=[]
        with open("../DataXml/data.csv","r") as f:
            csv_context=csv.reader(f)
            for csv_con in csv_context:
                ret_list.append(csv_con)
        print(ret_list)

cs=ReadCsv()
cs.read_csv()