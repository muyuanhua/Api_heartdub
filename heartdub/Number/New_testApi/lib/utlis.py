import xlrd
from openpyxl import load_workbook
import logging
import setting as setting


def case_data(dataname) -> list:
    """
    处理测试用例数据
    :param dataname: 测试用例文件名
    :return: 测试用例数据
    """
    test_case = 'D:\\PyApi_heartdub\\Number\\New_testApi\\database\\{}.xlsx'.format(dataname)
    test_num = Excel('r', test_case).read()
    testdata = excel_dict(test_num)
    return testdata
class Excel:
    """
    初始化方法 参数type：为r是读取excel，为w是写入excel,参数file_name是w文件路径
    """
    def __init__(self,type,file_name):
        """
        :param type: r:读 w:写
        :param file_name: 读取文件路径
        """
        if type=="r":
            #打开文件
            self.workbook=xlrd.open_workbook(file_name)
            #获取到所有的sheet_names获取到所有，得到的是一个list
            self.sheet_names=self.workbook.sheet_names()
            self.list_data=[]
        #写入excel
        elif type=="w":
            self.filename=file_name
            self.wb=load_workbook(self.filename)
            self.ws=self.wb.active

    def read(self):
        # 根据sheet_name去读取用例，并获取文件的总行数获取到每行的内容

        for sheet_name in self.sheet_names:
            # 通过每个sheetname获取到每个页的内容
            sheet=self.workbook.sheet_by_name(sheet_name)
            #获取总行数
            rosw=sheet.nrows
            #根据总行数进行读取
            for i in range(0,rosw):
                rowvalues=sheet.row_values(i)
                #将每行内容添加进去
                self.list_data.append(rowvalues)
            #     去除大标题第一行进行切割处理
         # 将得到的excel数据返回进行处理
        return self.list_data
    def write(self,data):
        """
        数据写入ex表内
        :param data: 需要写入的数据：list
        :return:
        """
        self.ws.append(data)
        self.wb.save(self.filename)
        logging.info("测试数据写入结果：写入成功")

def excel_dict(data):
    """
        1.将excel头部替换成英文的
        2.处理成json/dict格式
        """
    header={
        '用例编号': 'id',
        '用例请求类型': 'get_type',
        '测试url': 'url',
        '测试接口': 'interface',
        '用例标题': 'title',
        '测试数据': 'data',
        '预期结果': 'expected',
        '请求头': 'header',
        '响应数据状态/json返回数据的code': 'code',
        '状态码': 'status',
        '响应状态': 'msg',
        "前置条件":'precondition' #新增对新字段的处理

    }
    head=[]
    list_dict_data=[]
    for d in data[1]:
        # 获取到英文的头部内容如果为中文，则替换成英文 进行改成一个k
        # 传入两个参数的作用是 查到则返回查到的数据,查不到则返回传入的原数据
        d=header.get(d,d)
        # 将去除的头部英文装进list中
        head.append(d)
        # 获取到数据进行切片处理，0坐标为标题，1坐标是头部
    for b in data[2:]:
            # 头部和内容拼接为json串
        dict_data = {}
        for i in range(len(head)):
            # 之所以判断类型，如果不进行判断会出现str的错误，strip去除空格也有转str的用法
            if isinstance(b[i], str):
                dict_data[head[i]] = b[i].strip()
            else:
                dict_data[head[i]] = b[i]
        # list里面是字典格式
        list_dict_data.append(dict_data)
    return list_dict_data

def write_result(value1=None, value2=None, value3=None,
                 value4=None, value5=None, value6=None,
                 value7=None, value8=None) -> list:
    """
    将写入的值返回：为list格式
    :param value1: 值1 - 编号
    :param value2: 值2 - 测试接口名字
    :param value3: 值3 - 测试用例标题
    :param value4: 值4 - 测试url地址
    :param value6: 值5 - 测试数据/json
    :param value6: 值6 - 预计结果
    :param value7: 值7 - 实际结果
    :param value8: 值8 - 执行情况
    :return:
    """
    result_list = []
    result_list.append(value1)
    result_list.append(value2)
    result_list.append(value3)
    result_list.append(value4)
    result_list.append(value5)
    result_list.append(value6)
    result_list.append(value7)
    result_list.append(value8)
    return result_list

def get_test_url(msg):
    """
    返回不同环境的rul地址
    :param msg: loc：本地环境 uat:uat环境 dev:开发环境
    :return: url
    """

    if msg=="dev":
        return setting.BASE_URL_dev#读取setting.py文件内的变量
    elif msg=="uat":
        return setting.BASE_URL_uat
    elif msg == 'loc':
        return setting.BASE_URL




if __name__ == '__main__':
    # file = '../database/testcase.xlsx'
    # file = 'D:\\PyApi_heartdub\\Number\\New_testApi\\results\\results.xlsx'
    # e = Excel('w', file)
    # e.write(write_result(1, 2, 3, 4, 5, 6, 7, 0))
    file = '..\\database\\testcase.xlsx'
    e = Excel('r', file)
    list_read = e.read()
    a = excel_dict(list_read)
    # print(a)
    # print(a[0]["get_type"])  # 获取列表内第一个字典的get_type的值
    print(case_data('testcase'))









