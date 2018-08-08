import requests
from bs4 import BeautifulSoup

user_agent="Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;)"
headers={"User-Agent":user_agent}
url="https://bbs.pythontab.com/forum-3-{}.html"
for i in range(1,1):
	urlf=url.format(i)
	res=requests.get(urlf, headers=headers)
	soup=BeautifulSoup(res.text, "lxml")
	print(soup)
	titles=soup.find_all('a',{'class':'postTitle2'})
	for item in titles:
		title=item.text.strip()
		link=item['href']
		with open('blogs.txt', 'a+') as f:
		    f.write(title+'\n'+link+'\n')


