import requests
from bs4 import BeautifulSoup

user_agent="Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;)"
headers={"User-Agent":user_agent}
NAME=input("请输入搜索的关键字:")
url="http://search.17k.com/search.xhtml?c.st=0&c.q="
urlf=url+str(NAME)
print(urlf)
res=requests.get(urlf, headers=headers)
soup=BeautifulSoup(res.text, "lxml")
titles=soup.find_all('div',{'class':'textmiddle'})
for title in titles:
	title2=title.find('li',class_='bq').find('span',class_='ls').text
	title1=title.find('a').text.strip()
	print(title1,title2)
