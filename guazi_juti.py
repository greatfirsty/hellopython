from lxml import etree
import requests

url= 'https://www.guazi.com/sjz/8b948ce11209af53x.htm#fr_page=list&fr_pos=city&fr_no=1'
headers={


'Cookie':'uuid=fb67a2a1-49f4-4097-f690-2ff77475d180; antipas=6102492p2Z6a173t74F183210o1; ganji_uuid=3229077696612934519578; clueSourceCode=10103000312%2300; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22fb67a2a1-49f4-4097-f690-2ff77475d180%22%2C%22sessionid%22%3A%2241e2b95a-bdea-4f79-e296-40a119c7cc82%22%7D; user_city_id=12; preTime=%7B%22last%22%3A1556442494%2C%22this%22%3A1556442470%2C%22pre%22%3A1556442470%7D; lg=1; sessionid=41e2b95a-bdea-4f79-e296-40a119c7cc82; cityDomain=bj',
'Host':'www.guazi.com',
'Referer':'https://www.guazi.com/bj/?scode=10103000312&ca_s=pz_baidu&ca_n=tbmkbturl',

'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}
resp=requests.get(url,headers=headers)

p = etree.HTML(resp.text)
guazirenzheng = p.xpath("//div[@class='guazi-renzheng']/div[@class='bgbox']/dl[@class='pinggushi clearfix']/dd/div[@class='test-con']/text()")[0]
print(guazirenzheng)
dianpu = p.xpath("//div[@class='guazi-detail-baomai']/div[@class='baomai-right']/h3/text()")[0]
print(dianpu)
weizhi = p.xpath("//div[@class='guazi-detail-baomai']/div[@class='baomai-right']/p/text()")[0]
print(weizhi)
jibenxinxi = p.xpath("//ul[@class='basic-eleven clearfix']")
#具体太琐碎，就不做了


