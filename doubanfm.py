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
import subprocess

def getPlayList():
	url = nameV.aurl + nameV.murl + nameV.burl +nameV.token
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
    fileName = file_['url']
    print fileName
    #fileName = 'D:/githubworkspace/eric-doubanfm/p1022892.mp4'
    cmd = ['ffplay',fileName,'-nodisp','-autoexit']
    pro = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    try:
        pro.communicate()
    except Exception,e:
        pro.terminate()

getPlayList()