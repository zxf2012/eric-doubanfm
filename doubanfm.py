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
import pymedia.muxer as muxer
import pymedia.audio.acodec as acodec
import pymedia.audio.sound as sound
import os.path as path

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

def play(self):
    file_ = nameV.songList[0]
    #fileName = file_['url']
    fileName = 'D:/githubworkspace/eric-doubanfm/test.mp3'
    file_path = "/home/archy/Documents/python/yshouge.mp3"
    root,ext = path.splitext(fileName)
    demuxer = muxer.Demuxer(ext[1:].lower())
    decoder = None
    output = None

    file = open(file_path,'rb')
    data = ' '
    while data:
        data = file.read(20000)
        if len(data):
            frames = demuxer.parse(data)
            for frame in frames:
                if decoder == None:
                    decoder = acodec.Decoder(demuxer.streams[0])

                audio_frame = decoder.decode(frame[1])
                if audio_frame and audio_frame.data:
                    if output==None:
                        output = sound.Output(audio_frame.sample_rate,audio_frame.channels,sound.AFMT_S16_LE)

                    while self.stop:
                        time.sleep(1)

                    output.play(audio_frame.data)

            while output.isPlaying():
                time.sleep( 0.05 )

getPlayList()
	