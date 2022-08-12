import bs4
import requests

HEADERS = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}

KEYWORDS = ['Slave', 'VR', 'DALL', 'python']

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
  href = article.find(class_='tm-article-snippet__readmore').attrs['href']
  title = article.find('h2').find('span').text
  time = article.find('time').attrs['title']

  response_article = requests.get(base_url+href, headers=HEADERS)
  text_article = response_article.text

  soup_article = bs4.BeautifulSoup(text_article, features='html.parser')
  fulltext = soup_article.find(class_='tm-article-body').text

  if any(keyword in fulltext for keyword in KEYWORDS):
    result = f'{time} / {title} / {base_url + href}'
    print(result)
    continue