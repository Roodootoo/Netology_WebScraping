import bs4
import requests

HEADERS = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}

KEYWORDS = ['АйТи', 'VR', 'DALL', 'python']

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
  href = article.find(class_='tm-article-snippet__hubs-item-link').attrs['href']
  response = requests.get(base_url+href, headers=HEADERS)
  text = response.text
  soup = bs4.BeautifulSoup(text, features='html.parser')
  fulltext = soup.find('article-formatted-body article-formatted-body article-formatted-body_version-2')
  paragraphs = [paragraph.find('p').text for paragraph in fulltext]
  # previews = article.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
  # previews = [preview.find('p').text for preview in previews]
  for preview in previews:
    if any(keyword in preview for keyword in KEYWORDS):
      title = article.find('h2').find('span').text
      time = article.find('time').attrs['title']
      result = f'{time} / {title} / {base_url + href}'
      print(result)