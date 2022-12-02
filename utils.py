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


def getMultiCPU():
    print("searching CPU...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    # search AMD CPU
    AMDResults = soup.find("optgroup", label="AMD AM5 7000系列")
    for result in AMDResults:
        text = result.text
        if "AMD" in text:
            print(text)

    # search Intel CPU
    IntelResults = soup.find("optgroup", label="Intel Raptor Lake-s 13代1700 腳位『適700系列或兼容600系列主板』")
    for result in IntelResults:
        text = result.text
        if "Intel" in text:
            print(text)
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
