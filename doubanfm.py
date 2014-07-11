# -*- coding: UTF-8 -*-
#!/usr/bin/python
#Filename : doubanfm.py

import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8') 
import os
import nameV
import urllib  
import json
import pyglet


def getPlayList():
	url = nameV.aurl + nameV.murl + nameV.burl
	print '请求播放列表地址'
	print url
	page_source = None
	try:
		page_source = urllib.urlopen(url)
	except Exception, data:
		print Exception, ":", data
	pageData = page_source.read()
	jsonData = json.loads(pageData)
	nameV.songList = jsonData['song']
	printPlayList()
	
def printPlayList():
	print '------播放列表------'
	
	for song in nameV.songList:
		print song['title']
	print '------------------'
	play()

def play():
	file_ = nameV.songList[0]
	next_file = nameV.songList[1]
	#fileName = file_['url'] 
	#fileName = 'http://v.youku.com/v_show/id_XNzA1MDI2NDcy_ev_1.html'
	fileName = 'test.mp3'
	#source = pyglet.media.load('/Users/zxq517/Music/English/I Can.mp3', streaming=True)
	print file_['url'] 
	music = pyglet.resource.media(fileName, streaming=False)
	music.play()
	
	pyglet.app.run()

getPlayList()
	