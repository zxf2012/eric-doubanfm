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
	url = nameV.renrenurl
	print '请求播放列表地址'
	print url
	page_source = None
	try:
		page_source = urllib.urlopen(url)
	except Exception, data:
		print Exception, ":", data
	pageData = page_source.read()
	jsonData = json.loads(pageData)
	nameV.songList = jsonData['songs']
	printPlayList()

def printPlayList():
	print '------播放列表------'
	for song in nameV.songList:
	    print song['name'],song['artistName']
	print '------------------'
        while True:
            play()

def play():
    if len(nameV.songList) < 2:
        getPlayList()
    song = nameV.songList.pop(0)
    songSrc = song['src']
    songName = song['name']
    artistName = song['artistName']
    print '正在播放：',songName, '由',artistName,'演唱'
    #fileName = 'D:/githubworkspace/eric-doubanfm/p1022892.mp4'
    cmd = ['ffplay',songSrc,'-autoexit']
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    while True:
        print p.communicate()
    try:
        p.communicate()
    except Exception,e:
        p.terminate()

def main():
    getPlayList()
if __name__=='__main__':
    main()