
import requests
from bs4 import BeautifulSoup
url = "https://www.techtarget.com/searchenterpriseai/definition/AI-Artificial-Intelligence"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')

markup ="<p><!---this is a coment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


print(soup.prettify)
title = soup.title
print(title)
print(type(title))
print(type(title.string))
paras=soup.find_all('p')
print(paras)
anchors=soup.find_all('a')
print(anchors)

print(soup.find('p') )
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
     if(link.get ('href') != '#'):
         linktext = "https://www.techtarget.com/searchenterpriseai/definition/AI-Artificial-Intelligence" +link.get('href')     
         all_links.add (link)
         print(linktext)

print(soup. get_text())

navlinksTechtargetNetwork= soup.find("nav-links-TechtargetNetwork")
print(navlinksTechtargetNetwork)
#for elem in navlinksTechtargetNetwork.children:
    #print(elem)
