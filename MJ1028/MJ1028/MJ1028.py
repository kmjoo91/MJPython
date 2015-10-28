# -*- coding:utf-8 -*-
#참고 사이트 http://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
html_doc= """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story" name="parent">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
'''
soup = BeautifulSoup(html_doc,"html.parser")
#트리구조로 출력
print(soup.prettify())
#태그 안의 내용 출력
print(soup.title.string)
#특정태그 불러오기
print(soup.p)
print(soup.p['class'])
#특정태그를 모두 불러오기
print(soup('html')[0].contents)#하위계층 list
print(soup('a'))#모든 태그를 리스트로 반환
print(soup('a')[0].parent)#부모태그부터 출력
print(soup('a',{"id":"link1"}))#조건에 맞는 태그들을 list
#find & find_all & findAll 태그검색
print(soup.findAll("a"))
print(soup.find('a'))#print(soup.findAll('a')[0])과 같다고볼수있음
print(soup.find_all('a'))
print(soup.find('a')['href'])
'''
from urllib.request import urlopen
from urllib.parse import urljoin
import webbrowser
#웹툰 목록 가져오기
'''
url= "http://comic.naver.com/webtoon/list.nhn?titleId=651667&weekday=thu"
data = urlopen(url)
soup = BeautifulSoup(data, 'html.parser')
print(soup.encode('cp949'))
cartoons = soup.find_all('td',{'class':'title'})

for i in range(len(cartoons)):
    title = cartoons[i].find('a').string
    ref = cartoons[i].find('a')['href']
    print(ref)
    tempurl= urljoin(url,ref)
    print(title," ",tempurl)
    webbrowser.open_new(tempurl)
'''
class crawler:
    def crawl(self,pages,depth =10):
        for i in range(depth):
            newpage = set()
            for page in pages:
                try:
                    c = urlopen(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), from_encoding="utf-8")
                print('Found %s' % page)
            links = soup('a')
            for link in links:
                if('href' in dict(link.attrs)):
                    url= urljoin(page, link['href'])
                if url.find("'")!=-1 : continue
                url= url.split("#")[0]
                if url[0:4]=='http':
                    newpage.add(url)
            pages = newpage

pagelist = ['http://www.facebook.com']
crawl = crawler()
crawl.crawl(pagelist)
