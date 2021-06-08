import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
items = soup.select('html body h1')
for item in items:
    print(item.get_text())
