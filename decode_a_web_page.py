
'''import requests
url = 'http://github.com'
r = requests.get(url)
r_html = r.text
print(r_html)'''

'''from bs4 import BeautifulSoup
import urllib2#to open a web page
import urllib
import requests
url = 'http://github.com'
r = requests.get(url)
r_html = r.text
  # some requests code here for getting r_html 

soup = BeautifulSoup(r_html,"lxml")
title = soup.find('span', 'articletitle')'''

'''from bs4 import BeautifulSoup
import urllib2
#url = "https://www.goodreads.com/quotes/tag/love"
url = 'http://github.com'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
for anchor in soup.find_all('p'):
    #print(anchor.get('href', '/')) 
    print(anchor)'''



from bs4 import BeautifulSoup
import urllib2#to open a webpage
#url = "https://www.goodreads.com/quotes/tag/love"
url = 'https://www.nytimes.com/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
for anchor in soup.find_all('title'):
    #print(anchor.get('href', '/')) 
    print(anchor)