import os
import requests
import time
from lxml import etree
novel_list =[]
def get_novel():
    for i in range(1, 3):
        url = 'http://www.xbiquge.la/fenlei/1_{}.html'.format(i)
        res =requests.get(url)
        res = res.content
        rep = etree.HTML(res)
        novels = rep.xpath("//div[@class='l']/ul/li")
        for i in novels:
            novel = i.xpath("span[@class='s2']/a/@href")[0]
            novel_list.append(novel)
    return novel_list
def get_zj(name):
    time.sleep(5)
    rep = requests.get(name)
    rep = rep.content.decode()
    res = etree.HTML(rep)
    zhangjie = res.xpath("//div[@id='list']/dl/dd")
    # 这里得到具体章节
    zj_list = []
    for i in zhangjie:
        zj = i.xpath("a/@href")[0]
        zj = 'http://www.xbiquge.la' + zj
        zj_list.append(zj)
    return zj_list
def get_content(zj):
    res = requests.get(zj)
    res = res.content
    rep = etree.HTML(res)
    text_list=[]
    zj_name = rep.xpath("//div[@class='bookname']/h1/text()")[0]
    for text in rep.xpath("//*[@id='content']/text()"):
        text = text.strip('\r\n',).strip('\xa0\xa0\xa0\xa0')
        text_list.append(text)
    n_name = rep.xpath("//div[@class='con_top']/a[3]/text()")[0]
    return (n_name,zj_name,text_list,)


def save(bookname, name, texts):
    try:  # 文件夹不存在则以小说名字创建
        if not os.path.exists('./' + bookname):
            os.makedirs('./' + bookname)
        with open('./%s/%s.txt' % (bookname, name), 'w', encoding='UTF-8') as f:
            f.write(name + '\n')
            for text in texts:
                f.write(text + '\n')
        f.close()
        return True
    except Exception as e:
        print(e)
        return False
if __name__ == '__main__':

    book_list = get_novel()
    for i in book_list:
        rep = get_zj(i)
        for i in rep:
            bookname, name, texts=get_content(i)
            save(bookname, name, texts)
#出现的问题，没有用多线程进行任务，速度比较慢，另外，下载的书籍章节顺序乱了，需要Order
#针对问题，要考虑在哪里进行多线程处理
#个人考虑使用消息队列
