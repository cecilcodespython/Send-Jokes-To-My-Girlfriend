import requests
from bs4 import BeautifulSoup
import json


def collect_puns():
    url = 'https://www.luvze.com/love-jokes/'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=header)
    soup = BeautifulSoup(response.text,'lxml')
    jokes = soup.find_all('p')
    jokes = jokes[9:143]
    collection = list()
    for joke in jokes:
        data = {
            'pun':joke.get_text()
        }
        collection.append(data)

    return collection


if __name__ =="__main__":
    puns = collect_puns()
    with open("puns.json",mode="w") as pun_file:
        json.dump(puns,pun_file,ensure_ascii=False)
