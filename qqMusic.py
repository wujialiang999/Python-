import requests
import re
from urllib.request import quote
import json
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
def getjson(jsontext):
    rejson=json.loads(re.findall(r"^\w+\((.*)\)$", jsontext)[0])
    return rejson
def getMusicList(word,sum=20):
    #word="演员"
    url="https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=58294319880195336&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n="+str(sum)+"&w="+word+"&g_tk=5381&jsonpCallback=MusicJsonCallback10263594486078043&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"
    t=requests.get(url,headers=headers)
    t.encoding=t.apparent_encoding
    a=t.text
    musiclist=json.loads(re.findall(r"^\w+\((.*)\)$",a)[0])
    return musiclist
#获取songmid
def getSongmid(MusicList):
    mysongmid = []
    musicName=[]
    singerName=[]
    MusicListdata=MusicList.get("data")
    MusicListSong=MusicListdata.get("song")
    MusicListList=MusicListSong.get("list")
    for i in MusicListList:
        #mysongmid.append(i.get("file").get("strMediaMid"))
        mysongmid.append(i.get("mid"))
        musicName.append(i.get("name"))
        singerName.append(i["singer"][0].get("name"))
    return mysongmid, musicName, singerName
def getRsult(number,songmid):
    mid=songmid[number]
    url="https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?cid=205361747&guid=0&songmid={}&filename=0.m4a&callback=jQuery33109612115109632668_1540962383805&_=1540962383806".format(mid)
    Svkey=requests.get(url,headers).text
    dictData=getjson(Svkey)
    items=dictData.get("data").get("items")[0]
    vkey=items.get("vkey")
    musicmid=items.get("songmid")
    liuchang="http://streamoc.music.tc.qq.com/C400{}.m4a?guid=0&uin=0&fromtag=53&vkey={}".format(musicmid,vkey)
    putong="http://streamoc.music.tc.qq.com/M500{}.mp3?guid=0&uin=0&fromtag=53&vkey={}".format(musicmid,vkey)
    gaopin="http://streamoc.music.tc.qq.com/M800{}.mp3?guid=0&uin=0&fromtag=53&vkey={}".format(musicmid,vkey)
    wusun="http://streamoc.music.tc.qq.com/F00{}.flac?guid=0&uin=0&fromtag=53&vkey={}".format(musicmid,vkey)
    # print(dictData)
    # print(items)
    print("流畅音质:",liuchang)
    print("普通音质:",putong)
    print("高品质:",gaopin)
    print("无损音质:",wusun)
songName=input("请输入想下载的的歌曲或者歌手名字:")
musiclist=getMusicList(songName)
songmid,musicName,singer=getSongmid(musiclist)
print("id-歌曲名-歌手")
for i in range(len(songmid)):
    print(str(i),musicName[i],"-",singer[i])
id=int(input("输入想下载的歌曲ID:"))
getRsult(id,songmid)
