#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib


def getHtml(url):
	page = urllib.urlopen(url)	
	html = page.read()
	return html

def content(html):
	str = '<div class="msgCnt">'
	content = html.partition(str)[2]
	str1 = '<div class="pubInfo c_tx5">'
	content = html.partition(str1)[0]
	return content

def title(content, beg = 0):
	try:
		title_list = []
		while True:
			num1 = content.index('】', beg) +3
			num2 = content.index('</div>', num1)
			title_list.append(content[num1:num2])
			beg = num2
	
	except ValueError:
		return title_list

def data_out(neirong):
	with open("/home/joan/project/pyweather/data.txt","a+") as fo:
		fo.write('\n')
		for size in range(0, len(title)):
			fo.write(title[size]+ '\n')
		

qq_whe = content(getHtml("http://e.t.qq.com/dgtqyb"))
title = title(qq_whe)
data_out(title)
