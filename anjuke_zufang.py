# -*- coding: UTF-8 -*-
import csv
import time
from lxml import etree
import requests

def start_req(url,headers):
    resp = requests.get(url=url,headers=headers)
    p = etree.HTML(resp.text)
    html = p.xpath("//div[@id='list-content']/div[@class='zu-itemmod']")
    list1=[]
    for i in html:
       # title = i.xpath("div[@class='zu-info']/h3/a/@title")[0]
       # price = i.xpath("div[@class='zu-side']/p")
       # price = price[0].xpath('string(.)')
       # house_info= i.xpath("div[@class='zu-info']/p")[0]
      #  house_info = house_info.xpath("string(.)").strip()#消除空格
       # distance = i.xpath("div[@class='zu-info']/address[@class='details-item']/text()")[1].strip()
        url = i.xpath("div[@class='zu-info']/h3/a/@href")[0]
        list1.append(url)
    return list1

def next(msg):
    dt = msg
    print(dt)
    data={}
    for i in dt:
        time.sleep(6)
        req = requests.get(i,headers)
        p = etree.HTML(req.text)
        url =i
        title = p.xpath("//div[@class='wrapper']/h3[@class='house-title']/text()")[0]
        square = p.xpath("//ul[@class='house-info-zufang cf']/li[@class='house-info-item'][1]/span[@class='info']/text()")[0]
        pay_way = p.xpath("//ul[@class='house-info-zufang cf']/li[@class='full-line cf']/span[@class='type']/text()")[0]
        price = p.xpath("//ul[@class='house-info-zufang cf']/li[@class='full-line cf']/span[@class='price']/em/text()")[0]
        upstairs = p.xpath("//ul[@class='house-info-zufang cf']/li[@class='house-info-item l-width'][2]/span[@class='info']/text()")[0]
        xiaoqu = p.xpath("//ul[@class='house-info-zufang cf']/li[@class='house-info-item l-width'][3]/a[@class='link']/text()")[0]
        try:
         czyq = p.xpath("//div[@class='houseInfo-desc']/div[@class='houseInfo-item'][3]/div[@class='houseInfo-item-desc']/text()")[0].strip()
        except Exception as e:
            czyq = '无出租要求'
        datetime = p.xpath("//div[@class='mod-title bottomed']/div[@ class='right-info']/text()")[0]
        datetime = datetime.encode().decode()
        dt = datetime.split('：')
        date_time = dt[1]
        #联系人电话 这个有点难度先略过
        #这个可能需要phtomjsa
        data={
            '链接':url,
            '标题':title,
            '价格':price,
            '面积':square,
            '支付方式':pay_way,
            '楼层':upstairs,
            '小区':xiaoqu,
            '出租要求':czyq,
            '发布时间':date_time
        }
        print(data)
    return data
def xie_ru(msg):
    with open(r'C:\Users\hss\Desktop\python面试题\anjuke.csv','wb')as f:
        csvWriter = csv.writer(f)
        for k, v in msg.iteritems():
            csvWriter.writerow([k, v])
if __name__ == '__main__':
    url = 'https://bj.zu.anjuke.com/fangyuan/chaoyang/l2/'
    headers = {
        'cookie': 'ctid=14; aQQ_ajkguid=7F9CDE46-2EF4-A2AC-E124-C3F5052CFCF1; wmda_uuid=0284538a836d0fef4b56169290fa0638; wmda_visited_projects=%3B6289197098934; twe=2; ajk_member_captcha=6e294623e8e7fe517450fa242e1e4a5d; sessid=5B38D064-6FAB-B938-913A-4AA21AF691A7; lps=http%3A%2F%2Flogin.anjuke.com%2Flogin%2Fiframeform%3Fforms%3D10%26third_parts%3D000%26other_parts%3D000%26multi_form%3D1%7Chttps%3A%2F%2Fbj.zu.anjuke.com%2Fgfangyuan%2F1282243339%3Fshangquan_id%3D687%26from%3DFilter_5; 58tj_uuid=c5ce6055-9e40-45ee-bbad-eedd141f73cf; _ga=GA1.2.1092603964.1556529401; _gid=GA1.2.1977162765.1556529401; als=0; lui=159263518%3A1; new_uv=2; __xsptplus8=8.2.1556533312.1556533312.1%234%7C%7C%7C%7C%7C%23%23AKN57yXV9AtUz7fmvUKg0ND8kjiRMQdt%23; ajk_member_id=159263518; ajk_member_name=U1556530331704; ajk_member_key=13a54c168090e49e656ac7959931b9bb; ajk_member_time=1588069320; aQQ_ajkauthinfos=%2Fh8cMB2X3raDPoIj%2BweZE0O4pe4gzT%2FPR3D1uYrQFOGVxJ9b3HXIbhD%2FLwU3RFyOFUgidNC1rXEQy7uIyoU%2FJ2dER%2Fw',
        'referer': 'https://bj.zu.anjuke.com/fangyuan/chaoyang/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }
    t = start_req(url=url,headers=headers)
    dd = next(t)
#这一步写入
#最好搞个队列

