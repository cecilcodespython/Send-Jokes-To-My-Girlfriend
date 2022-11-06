import json
import random

trailing_message = [
    "Hope You liked this one",
    "hahaha im very funny",
    "I can see you smile from here",
    "I love you",
    "hope this made your day better",
    "your my angel,never forget",
    "i love your smile",
    "smileeeeeeeeeeeee"

]

random_trailing_message = random.choice(trailing_message)
def collect_pun():
    with open("puns.json") as puns_file:
        puns = json.load(puns_file)

    return puns

def get_random_pun():
    puns = collect_pun()
    pun =  random.choice(puns)
    return pun['pun']


def create_message():
    pun = get_random_pun()[3:]

    return f"{pun}\n\n Your Funny Boyfriend's Bot - Cecil"
