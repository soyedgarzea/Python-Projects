import pprint
from typing import Any
import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://news.ycombinator.com/news', timeout=1000)
soup = BeautifulSoup(markup=response.text, features='html.parser')
titles = soup.select(selector='.titleline > a')
# scores = soup.select(selector='.score')

# for title, score in zip(titles, scores):
#     print(f'{title.text} - {score.text}')

subtext = soup.select('.subtext')


def create_custom_hn(links: list[Any], subtext: list[Any]) -> list[Any] | None:
    hn: list[Any] = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'votes': points})

    return sorted(hn, key=lambda k: k['votes'], reverse=True)


pprint.pprint(create_custom_hn(titles, subtext))
