# -*- coding: utf-8 -*-

import string
import urllib2
import re


class HTML_Tool:
    BgncharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>|<jpg.*?>)")
    EndcharToNoneRex = re.compile("<.*?>")
    BgnParRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]
    def Replace_Char(self,x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub("\n    ", x)
        x = self.CharToNewLineRex.sub("\n", x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x = x.replace(t[0],t[1])
            return x
class Baidu_spider:
    def __init__(self,url):
        self.myUrl = url + '?see_lz=1'
        self.datas = []
        self.myTool = HTML_Tool()
        print u'已经启动爬虫..............'
    def baidu_tieba(self):
        myPage = urllib2.urlopen(self.myUrl).read().decode("utf-8")
        endPage = self.page_counter(myPage)
        title = self.find_title(myPage)
        print u'文章名称' + title
        self.save_data(self.myUrl,title,endPage)
    def page_counter(self,myPage):
        myMatch = re.search(r'class="red">(\d+?)</span>',myPage,re.S)
        if myMatch:
            endPage = int(myMatch.group(1))
            print u'发现 %d 页内容' % endPage
        else:
            endPage = 0
            print u'无法搜索到页数.......'
        return endPage
    def find_title(self,myPage):
        myMatch = re.search(r'<h3.*?>(.*)</h3>',myPage,re.S)
        title = u'暂无标题......'
        if myMatch:
            title = myMatch.group(1)
        else:
            print u'无法加载标题.......'
        # 文件名不能包含以下字符： \ / ： * ? " < > |
        title = title.replace('\\','').replace('/','').replace(':','')\
            .replace('*','').replace('?','').replace('"','').replace('<','')\
            .replace('>','').replace('|','')
        return title
    def save_data(self,url,title,endPage):
        self.get_data(url,endPage)
        f = open(title + '.txt', 'w+')
        f.writelines(self.datas)
        f.close()
        print u'文件已下载........'
        print u'按任意键退出.........'
        raw_input();
    def get_data(self,url,endPage):
        url = url + '&pn='
        for i in range(1,endPage+1):
            print u'爬虫通道 %d 正在工作中.....' %i
            myPage = urllib2.urlopen(url + str(i)).read()
            self.deal_data(myPage.decode('utf-8'))
    def deal_data(self,myPage):
        myItems = re.findall('id="post_content.*?>(.*?)</div>',myPage,re.S)
        for item in myItems:
            data = self.myTool.Replace_Char(item.replace("\n","").encode('utf-8'))
            self.datas.append(data+'\n')

print u"""#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.5
#   作者：Alexanderklau
#   日期：2016-09-16
#   语言：Python 2.7
#   操作：输入网址后自动只看楼主并保存到本地文件
#   功能：将楼主发布的内容打包txt存储到本地。
#---------------------------------------
"""
print u'请输入贴吧的地址最后的数字串：'
bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))

# 调用
mySpider = Baidu_spider(bdurl)
mySpider.baidu_tieba()