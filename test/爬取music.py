import re

pattern1 = r'id=([\d]+)">'
pattern2 = r'<li><a href=".*id=\d+">(.*)</a></li>'
#<li><a href="/song?id=571338279">往后余生（翻自 马良）</a></li>
#top100对应的id
id_detail = []
with open('../download/toplist.html', mode='r',encoding='utf-8') as fp:
    content = fp.read()
    id_list = re.findall(pattern=pattern1, string=content)
    name_list = re.findall(pattern=pattern2, string=content)
    for i in id_list:
        if len(i) == 9:
            id_detail.append(i)

#id清单
total_id = id_detail[1:]
#歌名&id清单
music_list = []
for i in range(len(total_id)):
    music_list.append(total_id[i])
    for j in range(len(name_list)):
        if j == i:
            music_list.append(name_list[j])
print(music_list)
print(len(music_list))
import urllib.request

url = 'http://music.163.com/song/media/outer/url?id=%s.mp3'
num = int(input('请输入你想下载top100的几首：'))
download_list = music_list[:2*num]
for i in range(num):
    real_url = url % (download_list[i*2])
    # try:
    urllib.request.urlretrieve(url = real_url,filename='../download/top100/%s.mp3'% (download_list[i*2+1]))
    # except Exception as e:
    #     pass

