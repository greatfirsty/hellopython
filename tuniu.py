from lxml import etree
from bs4 import BeautifulSoup
import js2xml
import requests

url='http://hotel.tuniu.com/hotel/list_iframe?city=200&checkindate=2019-05-04&checkoutdate=2019-05-05&keyword='
headers={
'Cookie': 'tuniuuser_citycode=MjAw; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; tuniu_partner=MTQwMCwwLCwzMTExMWViZjMxNTgyMWUxOTcwZWE0YTAzNzZhMDRjMw%3D%3D; _tacau=MCxmZWI4N2Q3Zi00OGQyLTQwM2MtYzcxZi0yMDkxZTI5MjllYTQs; _tact=ODk2NmJlNTAtNDQ0My0yMmY0LThjYmQtOTNjODIyMzM4ZmJi; _tacz2=taccsr%3Dbaidu%7Ctacccn%3D%28organic%29%7Ctaccmd%3Dmkt_06002401%7Ctaccct%3D%2525E9%252580%252594%2525E7%252589%25259B%2525E6%252597%252585%2525E6%2525B8%2525B8%2525E7%2525BD%252591%7Ctaccrt%3D%28none%29; _taca=1556873527993.1556873527993.1556873527993.1; _tacb=M2E0NzJhZjUtYWFjOC05NWY4LTZkZTItYmJkMTNiNDc4MWY0; _tacc=1; PageSwitch=1%2C213612736; __utma=1.99986577.1556873529.1556873529.1556873529.1; __utmc=1; __utmz=1.1556873529.1.1.utmcsr=baidu|utmccn=brand|utmcmd=brand|utmctr=%E9%80%94%E7%89%9B%E6%97%85%E6%B8%B8%E7%BD%91; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1556873529; OLBSESSID=r2vvonrso0iterbqr3uvl4ed55; tuniu_searched=a%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A6%3A%22%E5%8C%97%E4%BA%AC%22%3Bs%3A4%3A%22link%22%3Bs%3A50%3A%22http%3A%2F%2Fwww.tuniu.com%2Fg200%2Fwhole-bj-0%2Flist-h0-j0_0%2F%22%3B%7D%7D; MOBILE_APP_SETTING_OPEN-126=1; isHaveShowPriceTips=1; tuniuuser_ip_citycode=MjAw; hotel_checkindate=2019-05-04; hotel_checkoutdate=2019-05-05; __utma=1.99986577.1556873529.1556873529.1556873529.1; __utmc=1; __utmz=1.1556873529.1.1.utmcsr=baidu|utmccn=brand|utmcmd=brand|utmctr=%E9%80%94%E7%89%9B%E6%97%85%E6%B8%B8%E7%BD%91; UM_distinctid=16a7ce50111600-02532d105778c5-3e385e0c-100200-16a7ce501128d4; CNZZDATA5726564=cnzz_eid%3D1174976800-1556870598-http%253A%252F%252Fwww.tuniu.com%252F%26ntime%3D1556870598; fp_ver=4.7.1; BSFIT_EXPIRATION=1556914639593; BSFIT_OkLJUJ=FHFFCnknL-o5bRSI5BLbZ0nRVV9vEfUl; BSFIT_DEVICEID=GvPdjwlHiUDJCyZ76z9hSWlE64277FYP2lDKtLRNYlCovVCyEOZqS7v1K8q6b-KmpNoIJd2wAZdD6ycR7SgbxBzBsm3GoWvIQ7i5rIVqGONXQMmPDwqVVug5MO8Rk1_pPUHGD3C4HC00bswmmTQOP4-gNig7RuwR; __utmb=1.2.10.1556873529; __xsptplus352=352.1.1556873534.1556873730.2%231%7Cbaidu%7Cbrand%7Cbrand%7C%25E9%2580%2594%25E7%2589%259B%25E6%2597%2585%25E6%25B8%25B8%25E7%25BD%2591%7C%23%23Ut_C1T0sii6u6C7-BkuuijGkH1Ey-YML%23; MOBILE_APP_SETTING_STATE-126=CLOSE; Hm_lpvt_51d49a7cda10d5dd86537755f081cc02=1556873962; __utmb=1.3.10.1556873529; _pzfxuvpc=1556873528660%7C7001987382100307498%7C5%7C1556873963689%7C1%7C%7C1475546543120999364; _pzfxsvpc=1475546543120999364%7C1556873528660%7C5%7Chttps%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDuykY0CgGB00VIAs0k0TkT0000024kcdC00000TlEXRt.THLPE_yWs_5H1_L30A3qrHn1rj0YnWKxpA7EgLKM0ZnquHFhuHuWnWfsnj0kPjTYrfKd5H0dPH6vrDDLwjn4P1NAnHmLrHc3PY77njF7fHfLPYnY0ADqI1YhUyPGujY1nWnvP1nvnHf3FMKzUvwGujYkP6K-5y9YIZ0lQzqLILT8IZN8pgR8mvqVQ1qs5HDYnj0hmvdspyfqUyVYg10vnj0zPj0kFMNYUNq1ULNzmvRqmh7GuZRhIgwVgvd-uA-dUHdBTh78uaudIAdxmv7VTA7Guv3qmMF9Uhf0mLFW5HTkrHc%26tpl%3Dtpl_11534_19713_15764%26l%3D1512272302%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E9%252580%252594%2525E7%252589%25259B%2525E6%252597%252585%2525E6%2525B8%2525B8%2525E7%2525BD%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E8%2525AE%2525A9%2525E6%252597%252585%2525E6%2525B8%2525B8%2525E6%25259B%2525B4%2525E7%2525AE%252580%2525E5%25258D%252595%252520%2525E8%2525A6%252581%2525E6%252597%252585%2525E6%2525B8%2525B8%252520%2525E6%252589%2525BE%2525E9%252580%252594%2525E7%252589%25259B%2525EF%2525BC%252581%2526xp%253Did(%252522m3236736148_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D166%26wd%3D%25E9%2580%2594%25E7%2589%259B%25E6%2597%2585%25E6%25B8%25B8%25E7%25BD%2591%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3D93380420_hao_pg%26oq%3D%2525E9%2525A9%2525AC%2525E8%25259C%252582%2525E7%2525AA%25259D%26inputT%3D73510%26prefixsug%3Dtuniu%26rsp%3D3; hotel_order_begin_date=2019-05-04; hotel_order_end_date=2019-05-05; rg_entrance=010000%2F003001%2F000013%2F000000',
'Host': 'hotel.tuniu.com',
'Referer': 'http://www.tuniu.com/g200/hotel-bj-0/',

'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}
response= requests.get(url=url,headers=headers)
resp = BeautifulSoup(response.content,'lxml')
pp = resp.select('script')[8].string
content = js2xml.parse(pp,encoding='utf8',debug=False)

parse_tree = js2xml.pretty_print(content)
print(parse_tree)
selector = etree.HTML(parse_tree)
html = selector.xpath("//property[@name='list']/array/object")

for i in html:
    name = i.xpath("property[@name ='name']/string/text()")[0]
    print(name)
    url = i.xpath("property[@name = 'url']/string/text()")[0]
    url = 'https://hotel.tuniu.com'+url
    print(url)
    level = i.xpath("property[@name='levelInfo']/object/property[@name='name']/string/text()")[0]
    print(level)
    address = i.xpath("property[@name = 'address']/string/text()")[0]
    print(address)
    addressInfo = i.xpath("property[@name = 'addressInfo']/string/text()")[0]
    print(addressInfo)
    position_lng = i.xpath("property[@name = 'pos']/object/property[@name ='lng']/string/text()")[0]
    position_lat = i.xpath("property[@name = 'pos']/object/property[@name ='lat']/string/text()")[0]
    print(position_lat)
    #剩下的不想写了，无非从里面找找数据
    #傻逼了，我以为数据都是放在script里面呢，谁知道都放在ajax里呢，直接通过链接获取数据就可以了
    #url='https://hotel.tuniu.com/ajax/list?search%5BcityCode%5D=200&search%5BcheckInDate%5D=2019-05-05&search%5BcheckOutDate%5D=2019-05-06&search%5Bkeyword%5D=&suggest=&sort%5Bfirst%5D%5Bid%5D=recommend&sort%5Bfirst%5D%5Btype%5D=&sort%5Bsecond%5D=&sort%5Bthird%5D=cash-back-after&page=3&returnFilter=0'



