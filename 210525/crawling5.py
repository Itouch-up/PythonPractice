import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')

section = soup.find('ul', id='hobby_course_list')
titles = section.find_all('li', 'course')
for index, title in enumerate(titles):
    print(str(index+1)+'.', title.get_text().split('[').split('-')[-1].strip())
