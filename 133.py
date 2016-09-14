# -*- coding: utf-8 -*-
import urllib2
import re
import thread
import time
import urllib

class Spider_Model:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    def Getpage(self,page):
        myUrl = "http://www.qiushibaike.com/hot/page/" + page
        user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.6) Gecko/20070914 Firefox/2.0.0.7'
        headers = {'user-Agent': user_agent}
        req = urllib2.Request(myUrl,headers=headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        unicodepage = myPage.decode('utf-8')

        myItems = re.findall('<div.*?class="content">(.*?)</div>',unicodepage,re.S)
        return myItems
    def load_page(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    myPage = self.Getpage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print '无法链接网络！'
            else:
                time.sleep(5)
    def showPage(self,nowPage,page):
        i = 0
        # print len(nowPage)
        for i in range(0, len(nowPage)):
            if i < len(nowPage):
                print u'第%d页,第%d个故事' % (page, i), nowPage[i].replace("\n\n", "")
                i += 1
            else:
                break

    def Start(self):
        self.enable = True
        page = self.page

        print u'正在加载中.......loading'
        thread.start_new_thread(self.load_page,())
        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.showPage(nowPage,page)
                page += 1


print u"""
---------------------------------------
   程序：糗百爬虫
   版本：0.3
   作者：Alexanderklau
   日期：2016-09-14
   语言：Python 2.7
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
"""

print u'请按下回车浏览今日的糗百内容：'
raw_input(' ')
myModel = Spider_Model()
myModel.Start()
