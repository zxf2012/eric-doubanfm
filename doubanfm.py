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
from select import select

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
    cmd = ['ffplay',songSrc,'-autoexit']
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    try:
        p.communicate()
    except Exception,e:
        p.terminate()
def control(self,r):
    rlist, _, _ = select([sys.stdin], [], [], 1)
    if rlist:
        s = sys.stdin.readline().rstrip()
        if s:
            if s == 'n':
                print '下一首...'
                #self.skip_mode = True
                return 'next'
            elif s == 'f' and self.private:
                print '正在加心...'
                #self.user.fav_song(r['sid'], r['aid'])
                print "加心成功:)\n"
                return 'fav'
            elif s == 'd' and self.private:
                print '不再收听...'
                #self.songlist = self.user.del_song(r['sid'], r['aid'])
                print "删歌成功:)\n"
                return 'del'
            elif s == 'p' and not self.pause:
                print '已暂停...'
                print '输入p以恢复播放\n'
                return 'pause'
            elif s == 'r' and self.pause:
                print '恢复播放...'
                print '继续享受美妙的音乐吧:)\n'
                return 'resume'
            else:
                print '错误的操作，请重试\n'

def main():
    getPlayList()
if __name__=='__main__':
    main()