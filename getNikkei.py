# coding: UTF-8

import urllib.request, urllib.error
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.nikkei.com/markets/kabu/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# タイトルを文字列を出力
print (soup.title.string)