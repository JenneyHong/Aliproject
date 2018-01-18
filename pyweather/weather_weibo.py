#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import string
import sys
import os
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
from lxml import etree


reload(sys)
sys.setdefaultencoding('utf-8')
if(len(sys.argv) >=2):
	user_id = (int)(sys.argv[1])
else:
	user_id = (int)(raw_input(u"请输入user_id: "))

cookie = {"Cookie": "_T_WM=6458e497e7584907f35d4b2601624a6f; SCF=AlnwGS9mxFXaaK7VO4sh9HBsOg2nbgCXtLctEJUXGhB5Tywl0lk8N0CO9kiLgjRwu1kDnUGgdNDBtNsYtQ_JaX0.; H5_INDEX=3; H5_INDEX_TITLE=katherine-%E7%90%BC; expire=Tue, 09 Jan 2018 08:08:47 GMT; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3Dhotword%26luicode%3D20000173%26fid%3D102803_ctg1_8999_-_ctg1_8999_home%26uicode%3D10000011; SUB=_2A253UBr8DeRhGedJ6FYQ9CbJzT6IHXVUuqa0rDV6PUJbkdANLUn8kW1NVjhxQQKot-00vapYSSN07JMIt75UhPzh; SUHB=03o0NoBaCvr_1m; SSOLoginState=1515481772"}
url = 'http://weibo.cn/u%d?filter=1&page=1' % user_id

html = requests.get(url, cookies = cookie).content
selector = etree.HTML(html)
#pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])

result = ""
urllist_set = set()
word_count = 1

print u'爬虫准备就绪...'

for page in range(1, 3):
	url = 'http://weibo.cn/u/%d?filter=1&page=%d' % (user_id,page)
	lxml = requests.get(url,cookies = cookie).content

	selector = etree.HTML(lxml)
	content = selector.xpath('//span[@class="ctt"]')
	for each in content:
		text = each.xpath('string(.)')
		if word_count >=4:
			text = "%d :" % (word_count-3) + text + "\n\n"
		else:
			text = text +"\n\n"
		result = result + text
		word_count +=1

fo = open("/home/joan/project/pyweather/weatherdata_2.txt", "wb")
fo.write(result)
word_path=os.getcwd()
print u'文字微博爬取完毕'

