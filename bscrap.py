from bs4 import BeautifulSoup
from requests import get

url = 'https://www.kantipurdaily.com/news'
url2 = 'http://gorkhapatraonline.com/category/8'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
'''
movie_containers = html_soup.find('aside', class_ = 'col-xs-4 col-sm-4 col-md-4 scrollable')
print(len(movie_containers))
for i in movie_containers.find_all('div',  class_= 'item'):
    for n in i.find_all('p'):
        print(n.text)
        print('-------')
'''
items = html_soup.find('section', class_= 'listLayout')
news = items.find('div', class_= 'col-xs-10 col-sm-10 col-md-10')
for i in news.find_all('article'):
    for n in i.find_all('p'):
        data = n.text
        print(data.split('\n'))
