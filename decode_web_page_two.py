from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import urllib2
url="https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
#page=urllib2.urlopen(url)
#soup=BeautifulSoup(page.read())
#print(soup)
r=requests.get(url)
soup=BeautifulSoup(r.text)
all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")

for elem in all_p_cn_text_body[7:] :
	print(elem.text) 