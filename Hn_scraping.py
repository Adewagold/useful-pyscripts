import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")

links= soup.select('.storylink')
votes= soup.select('.score')

print(links[0])
print(votes[0])
print(votes[0].get("id"))