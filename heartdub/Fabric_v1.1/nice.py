# # # import requests
# # # import xlrd
# # # from xlutils.copy import copy
# # # book=xlrd.open_workbook("D:\\PyApi_heartdub\\Unittest_api\\test\\test_case.xls")
# # # table=book.sheet_by_name("Sheet1")
# # # # print(table)
# # # row_num=table.nrows
# # # col_num=table.ncols
# # # # print(row_num,col_num)
# # #
# # #
# # #
# # # def read_excel(row=None,col=None):
# # #     book = xlrd.open_workbook("D:\\PyApi_heartdub\\Unittest_api\\test\\test_case.xls")
# # #     table = book.sheet_by_name("Sheet1")
# # #     values=table.cell_value(row,col)
# # #     return values
# # #
# # #
# # # def request_values():
# # #     url_list=[]
# # #     method_list=[]
# # #     data_list=[]
# # #     for i in range(1,4):
# # #         if i < 4:
# # #             url_port=read_excel(i,3)
# # #             # print(read_excel(i,2))
# # #             url_list.append(url_port)
# # #             method=read_excel(i,2)
# # #             method_list.append(method)
# # #             data=read_excel(i,4)
# # #             data_list.append(data)
# # #     for url1 in url_list:
# # #         if url1!=None:
# # #             url = "http://one.heartdub.cn:8082"+url1
# # #     print(url)
# # #     print(data_list)
# # #     print(method_list)
# # #     print(data_list)
# # #
# # # def write_data(row,col,value):
# # #     read_data=xlrd.open_workbook("D:\\PyApi_heartdub\\Unittest_api\\test\\test_case.xls")
# # #     write_data=copy(read_data)
# # #     sheet_data=write_data.get_sheet(0)
# # #     sheet_data.write(row,col,value)
# # #     write_data.save("D:\\PyApi_heartdub\\Unittest_api\\test\\test_case.xls")
# # # if __name__ == '__main__':
# # #     print(request_values())
# # import requests
# #
# # url = "http://one.heartdub.cn:8082/pattern_info_select"
# # form = {"user_code": 202108111002491543221, "order_by": "time_des"}
# # res=requests.post(url,form)
# # r=(res.TypeError)
# # print(r)
#
#
#
#
#
# # import requests
# # import json
# #
# #
# # class RunMain():
# #     def send_post(self,url,data,header=None):
# #         result=requests.post(url=url,data=data,headers=header)
# #         return result.json()
# #
# #     def send_get(self,url,data,header=None):
# #         result=requests.get(url=url,params=data,headers=header)
# #         return result.json()
# #
# #     def run_main(self,method,url,data,header=None):
# #         result=None
# #         if method=="post":
# #             result=self.send_post(url,data)
# #         elif method=="get":
# #             result=self.send_get(url,data)
# #         else:
# #             print("method?????????")
# #         return result
# #
# #
# # if __name__ == '__main__':
# #     url="http://api.heartdub.cn:8080/login"
# #     data={"user_addr":"13668418734","user_pass":"myh123","auth_code":"150be7d0a3d711eb81d2d1264cd620fb"}
# #     result1=RunMain().send_post(url,data)
# #     print(result1)
# #
# #
# def add(a=None,b=None,c=None,d=None,e=None,F=None):
#
#     f=a+b+c+d+e+F
#
#     return f
# def ride(a,b):
#     c=a*b
#     return c
# def divide(a,b):
#     c=a/b
#     return c
#
# if __name__ == '__main__':
#     # print(divide())
#     print(ride(23,367))
#     # print(add(15500,2000,14000,1400,3000))
#     print(add("www.","heet",".com"))
# import logging
#
# # class Test(object):
# #     def __init__(self,num):
# #         self.num=num
# #
# #     def unnormal(self):
# #         try:
# #             print("??????????????????")
# #             r=10/self.num
# #             print("result:",r)
# #         except TypeError as e:
# #             print("TypeError:",e)
# #         except ZeroDivisionError as e:
# #             logging.exception(e)
# #         finally:
# #             print("finally finish")
# # if __name__ == '__main__':
# #
# #     op_test1=Test(num=2)
# #     op_test1.unnormal()
# #     op_test2=Test(num="test")
# #     op_test2.unnormal()
# #     op_test3=Test(num=0)
# #     op_test3.unnormal()
# # import xlrd
# #
# # workbook=xlrd.open_workbook("D:\PyApi_heartdub\Number\New_testApi\database\name.xls")
# # #??????????????????sheet_names????????????????????????????????????list
# # sheet_names=workbook.sheet_names()
# # list_data=[]
# import requests
#
# result=requests.post(url="http://api.heartdub.cn:8080/login",data="{'user_addr':'1127535539@qq.com','user_pass':'myh123','auth_code':'150be7d0a3d711eb81d2d1264cd620fb'}",headers="{'content-type':'multipart/form-data; boundary=--------------------------570229387831267734096418'}")
# print(result.json())
import hashlib
import datetime
# #import sys
# def Findmd5(args):
#     md=args.hashvalue
#     starttime=datetime.datetime.now()
#     for i in open(args.file):
#         md5=hashlib.md5()   #????????????md5??????????????????
#         rs=i.strip()    #????????????????????????
#         md5.update(rs.encode('utf-8'))  #??????????????????????????????
#         newmd5=md5.hexdigest()  #??????????????????16???????????????
#         #print newmd5
#         if newmd5==md:
#             print ('????????????'+rs)    #????????????????????????
#             break
#         else:
#             pass
#
#     endtime=datetime.datetime.now()
#     print(endtime-starttime)	#????????????????????????
#
# if __name__=='__main__':
#     import argparse #???????????????????????????
#     parser=argparse.ArgumentParser(usage='Usage:./findmd5.py -l ?????????????????? -i ????????? ',description='help info.')   #??????????????????????????????
#     parser.add_argument("-l", default='wordlist.txt', help="????????????.", dest="file")    #?????????????????????????????????????????????????????????
#     parser.add_argument("-i", dest="hashvalue",help="?????????????????????.")
#
#     args = parser.parse_args()  #???????????????
#     Findmd5(args)

header = {
        '????????????': 'id',
        '??????????????????': 'get_type',
        '??????url': 'url',
        '????????????': 'interface',
        '????????????': 'title',
        '????????????': 'data',
        '????????????': 'expected',
        '?????????': 'header',
        '??????????????????/json???????????????code': 'code',
        '?????????': 'status',
        '????????????': 'msg'
}
d=header.get(1,1)
print(d)

