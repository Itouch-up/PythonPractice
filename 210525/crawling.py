import requests
from bs4 import BeautifulSoup
res = requests.get('https://news.v.daum.net/v/20210524211809381')
soup = BeautifulSoup(res.content, 'html.parser')
mydata = soup.find('title')
print(mydata.get_text())
