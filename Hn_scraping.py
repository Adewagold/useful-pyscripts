import requests
from bs4 import BeautifulSoup
import pprint
from sys import argv
import time
page_number = argv[1]



def sort_stories_by_vote(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hacker_news(number):
    hn = []
    for i in range(int(number)):
        res = requests.get(f"https://news.ycombinator.com/news?p={i+1}")
        print("page Number "+str(i+1))

        soup = BeautifulSoup(res.text, "html.parser")

        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        for index, item in enumerate(links):
            title = links[index].getText()
            href = links[index].get('href', None)
            vote = subtext[index].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(" points", ''))

                if points > 99:
                    hn.append({'title': title, 'link': href, "votes": points})
        time.sleep(2)
    return sort_stories_by_vote(hn)


pprint.pprint(create_custom_hacker_news(page_number))