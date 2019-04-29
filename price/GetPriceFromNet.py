import time
import urllib
import urllib.request

from obj.PriceObj import *


def get_price_history_by_net(price_code, begin_date, end_date):
    """
    :param price_code: for example, sh000300 沪深300 sh000001 上证 sz9901219 深圳成指
    :param begin_date: 查询起始时间 for example, time.strptime('2016-09-02', '%Y-%m-%d')
    :param end_date: 查询截止时间 for example, time.strptime('2017-11-08', '%Y-%m-%d')
    :return:
    """
    request_id = __get_request_id(price_code)
    begin_date = time.strftime("%Y%m%d", begin_date)
    end_date = time.strftime("%Y%m%d", end_date)
    url = 'http://quotes.money.163.com/service/chddata.html?code=' \
          + request_id + '&start=' + begin_date + '&end=' + end_date + '&fields=TCLOSE;'
    data = __http_get(url).decode('gb2312')  # 该段获取原始数据
    print(data)
    data = data.split('\r\n')  # 按换行符分割原始数据
    price_data = data[1:]  # 真正的数据
    if price_data.__len__() == 0:
        print("获取不到交易数据，请确认类型及编码是否正确！price_code:[" + price_code + "]")
        raise
    price_data = [x.replace("'", '') for x in price_data]  # 去掉指数编号前的“'”
    price_obj_array = []
    price_data = [x.split(',') for x in price_data]
    for price_line_data in price_data:
        if price_line_data.__len__() > 3:
            price_obj = PriceObj(price_line_data[0], price_line_data[3])
            price_obj_array.append(price_obj)
    return price_obj_array


# 获取页面数据
def __http_get(url):
    print("请求地址：" + url)
    req = urllib.request.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    opener = urllib.request.urlopen(req)
    response_content = opener.read()
    return response_content


def __get_request_id(price_code):
    price_type = price_code[0:2]
    price_id = price_code[2:]
    if price_type == 'sh':
        return '0' + price_id
    if price_type == "sz":
        return '1' + price_id


get_price_history_by_net('sh000300',  time.strptime('2016-09-02', '%Y-%m-%d'),
                         time.strptime('2017-11-08', '%Y-%m-%d'))

# id: sh000300 沪深300 sh000001 上证 sz9901219 深圳成指
