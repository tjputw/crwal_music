import requests, re

url = 'https://music.163.com/discover/toplist'
headers = {
    'Host':'music.163.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer':'https://music.163.com/',
    'Accept':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'_iuqxldmzr_=32; _ntes_nnid=4e69cad491093fb87429e0dff72e9fe7,1530093155367; _ntes_nuid=4e69cad491093fb87429e0dff72e9fe7; WM_TID=1%2FWc8HK5sN7OWk%2FmU3VCCI9FKxqtRj9u; JSESSIONID-WYYY=rNpnfNytpUAxtNcqqHyHkxsVGRGUuNsfG%2FPj0Gj7%2BOvkmAmEaOa3X5A%2Bp6n0xe7%2B4UJGWkItKPVBXRijHMg%5Cq66kWZlfgKZ%2F1SmBByGK76uaZmp2h8gQNDfpr7RbWRl8f%2BSzw6uOhzdUERWHTr7oTjoRojzzncwVuV17hBD8wBhExSrX%3A1530099149072; __utma=94650624.698691635.1530093161.1530093161.1530098385.2; __utmz=94650624.1530098385.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=94650624; __utmb=94650624.12.10.1530098385',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
}
response = requests.get(url=url, verify=False, headers=headers)
response.encoding = 'utf-8'
res = response.text
# with open('../download/toplist.html','w',encoding='utf-8') as fp:
#     fp.write(res)

#<li><a href="/song?id=571338279">往后余生（翻自 马良）</a></li>
pattern = r'<a href="/song?id=([\d]+)">'
id_list = re.findall(pattern=pattern, string=res)
print(id_list)