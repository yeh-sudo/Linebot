import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, LocationSendMessage

import requests
from bs4 import BeautifulSoup

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

coolpc_url = 'https://www.coolpc.com.tw/evaluate.php'


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def test(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    location_message = LocationSendMessage(
        title='my location',
        address='Tokyo',
        latitude=35.65910807942215,
        longitude=139.70372892916203
    )
    line_bot_api.reply_message(reply_token, location_message)

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
