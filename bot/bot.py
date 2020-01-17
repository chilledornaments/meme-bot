import requests
import json

from random import choice
from time import sleep
from os import environ

RANDOM_MEME_LINK = "https://meme-api.herokuapp.com/gimme"

class MemeBot:


    def __init__(self):

        sleep(choice(range(1, 3600)))

        pass


    def get_trending(self):

        pass


    def pick_random_gif(self):

        pass

    
    def retrieve_meme(self):

        r = requests.get(RANDOM_MEME_LINK)

        if r.status_code != 200:
            print(f"Error getting random meme: {r.status_code} {r.text}")

        j = json.loads(r.text)

        self.post_to_slack(j['url'])


    def post_to_slack(self, link):

        h = {
            "Content-type": "application/json"
        }

        j = json.dumps({
            "channel": environ['SLACK_CHANNEL'],
            "icon_emoji": environ['SLACK_ICON_EMOJI'],
            "title": "Hot New Memes In Your Area",
            "username": environ['SLACK_USERNAME'],
            "text": link
        })

        r = requests.post(environ['SLACK_WEBHOOK'], data=j, headers=h)

if __name__ == "__main__":

    m = MemeBot()
    m.retrieve_meme()