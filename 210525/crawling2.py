import requests
from bs4 import BeautifulSoup
html = """<html>
  <body>
  <h1 id='title'>[1]크롤링이란?</h1>
  <p class=cssstyle>'웹페이지에서 필요한 데이터를 추출하는 것'</p>
  <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
</body>
<html>
"""
soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('p')
for item in data:
    print(item.string)
# print(data)
# print(data.string)
# print(data.get_text())
# class = class_='cssstyle','cssstyle'
# attrs={'align':'center'}
# id='body'
