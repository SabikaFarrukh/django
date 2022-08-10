import requests
from bs4 import BeautifulSoup
url = "https://www.techtarget.com/searchenterpriseai/definition/AI-Artificial-Intelligence"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')

markup ="<p><!---this is a coment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


#print(soup.prettify)
title = soup.title

#print(paras)
#print(anchors)
print(soup.find('p') )
print(soup.find('p')['class'])
print(soup.find_all("p",class_="lead"))
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
     if(link.get ('href') != '#'):
         linktext = "https://www.techtarget.com/searchenterpriseai/definition/AI-Artificial-Intelligence" +link.get('href')     
         all_links.add (link)
         print(linktext)



print(soup. get_text())
