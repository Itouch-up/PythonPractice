import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('#popular_srch_lst > li > span.txt')
for item in items:
    print(item.get_text())
