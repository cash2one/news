# -*- coding: utf-8 -*-
# @Author: huangnan
# @Date:   2016-10-20 20:07:43
# @Last Modified by:   HUANG NAN
# @Last Modified time: 2016-11-13 15:22:20
# @E-mail: foxstarx@gmail.com


from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.conf import settings
from pyquery import PyQuery as pq
import MySQLdb
import json
import os

thumbnail_url = settings.THUMBNAIL_URL
if not thumbnail_url.endswith(os.sep):
	thumbnail_url = thumbnail_url + os.sep

def Indexpage(require):

	def get_news_list(results):
		news_list = []

		for result in results:
			news_list.append(get_news_items(result))
		return news_list

	def get_news_items(result):
		item = {}
		item["title"] = result[0]
		item["uri"] = result[1]
		item["src_time"] = result[2]
		item["src"] = result[3]
		item["thumbnail_url"] = thumbnail_url
		if result[4].split(":")[0] == 'imgs':
			item["img"] = int(result[4].split(":")[-1])

		return item

	connstring = settings.DB_CONNECTSTRING
	try:
		conn = MySQLdb.connect(**connstring)
		cur=conn.cursor()
		count = cur.execute(settings.SQL_NEWSLIST)
		print 'there has %s rows record' % count

		results = cur.fetchall()
		cur.close()
		conn.close()

		news_list = get_news_list(results)

	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	# FieldList = [newitem1, newitem2]
	return render(require, 'home/index.html', {'news_list': news_list})

def Listpage(require, uri = ''):

	def dealcontent(filepath):
		#print 'subrespath: %s' % filename
		content = open(filepath).read()
		content = content.strip('\r')
		content = content.strip('\n')
		content = content.strip('\t')
		content = content.strip('\xc2\xa0')
		content = content.strip('\xe3\x80\x80')
		content = content.strip()
		#print 'type: %s\r\ncontent: %s' % (type(content), content)
		return content

	def gethtml(path):
		html = []
		for itempath in path:
			chapteridx = 1
			while True:
				if not itempath.endswith(os.sep):
					itempath = itempath + os.sep
				chapterpath = itempath + 'html' + os.sep + str(chapteridx) + '.txt'
				if not os.path.exists(chapterpath):
					break

				content = dealcontent(chapterpath)

				if '<img' in content:
					d = pq(content)
					if d('img').attr('src'):
						content = d('img').attr('src')
					elif d.attr('href'):
						content = d.attr('href')
					html.append(dict(type = 'img', content = content))
				elif 'strong' in content:
					html.append(dict(type = 'strong', content = pq(content).text()))
				else:
					html.append(dict(type = 'text', content = content))

				chapteridx += 1
		return html

	respath = settings.RESPATH + uri + os.sep
	path = []
	news = {}
	for file in os.listdir(respath):
		try:
			path.append(respath + str(int(file)))
		except:
			pass#print '%s cover to int error' % file
	print path

	content = json.loads(open(respath + 'readme.txt', 'r').read())

	news['title'] = content['_title']
	news['src'] = content['_src']
	news['src_time'] = content['_time']
	news['thumbnail_url'] = thumbnail_url

	return render(require, 'home/list.html', {'news': news, 'html': gethtml(path)})

import base64
import urllib2
from urllib import urlencode

def Testpage(require):

	req_url = settings.ADV_XIANGUO_URL
	app_id = settings.ADV_XIANGUO_APP_ID
	site_id = settings.ADV_XIANGUO_SITE_ID

	req_json = {}
	appinfo = {}
	networkinfo = {}

	appinfo['app_id'] = app_id
	appinfo['ad_type_id'] = site_id
	appinfo['app_version'] = '1.0'
	appinfo['ad_size'] = '414*100'
	appinfo['host_package_name'] = '591joy'

	networkinfo['ip'] = ''
	networkinfo['connection_type'] = 0

	req_json['app_info'] = appinfo
	req_json['network_info'] = networkinfo

	json_string = json.dumps(req_json, default = lambda obj:obj.__dict__, indent = 2)	
	post_data = urlencode({'json=': base64.b64encode(json_string)})

	req = urllib2.urlopen(req_url, post_data)
	print req
	content = req.read()

	print 'content: %s' % content

	return render(require, 'home/list.html', {})