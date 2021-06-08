import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('div.rgt > ul.lst_major > li')
for item in data:
    print("지수이름 : ", item.find('a').get_text(), " 현재지수 : ",
          item.find('span').get_text(), item.find('em').get_text())
