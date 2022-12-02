import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, LocationSendMessage, TemplateSendMessage

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


def getMultiMB():
    print("search Motherboard...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    X670Results = soup.find("optgroup", label="AMD X670E & X670 / AM5腳位(DDR5)")
    for result in X670Results:
        text = result.text
        if "X670" in text and "送" not in text and "活動" not in text:
            print(text)

    Z790Results = soup.find("optgroup", label="Intel Z790 / 1700 腳位 (DDR5)-12代.13代皆支援")
    for result in Z790Results:
        text = result.text
        if "Z790" in text and "送" not in text and "活動" not in text:
            print(text)


def getMultiRam():
    print("search Ram...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    DDR5Results = soup.find("optgroup", label="桌上型記憶體 DDR5 雙通道")
    for result in DDR5Results:
        text = result.text
        if "DDR5" in text:
            print(text)


def getMultiSSD():
    print("search SSD...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    SSDResults = soup.find("optgroup", label="M.2 PCIe 4.0 (Gen4) SSD固態硬碟")
    for result in SSDResults:
        text = result.text
        if "Gen4" in text:
            print(text)


def getMultiAirCooler():
    print("search Air Cooler...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    AirCoolerResults = soup.find("optgroup", label="Noctua 貓頭鷹 散熱器 【6年保固】")
    for result in AirCoolerResults:
        text = result.text
        if "貓頭鷹" in text:
            print(text)


def getMultiAIO():
    print("search AIO...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    AIOResults = soup.find("optgroup", label="恩傑 NZXT【立光代理 6年保固換新】")
    for result in AIOResults:
        text = result.text
        if "Kraken" in text:
            print(text)


def getMultiVGA():
    print("search VGA...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    RTX4080Results = soup.find("optgroup", label="NVIDIA RTX4080-16G")
    for result in RTX4080Results:
        text = result.text
        if "MHz" in text:
            print(text)

    RTX4090Results = soup.find("optgroup", label="NVIDIA RTX4090")
    for result in RTX4090Results:
        text = result.text
        if "MHz" in text:
            print(text)


def getMultiCase():
    print("search Case...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    LianLiResults = soup.find("optgroup", label="聯力工業 LANLI 機殼")
    for result in LianLiResults:
        text = result.text
        if "聯力" in text:
            print(text)


def getMultiPSU():
    print("search PSU...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    PSUResults = soup.find("optgroup", label="華碩 ASUS【0800到府收送】")
    for result in PSUResults:
        text = result.text
        if "華碩" in text:
            print(text)


def getCPU(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n4"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            print(c.text)
            found = True


def getMB(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n5"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text and "升級" not in text:
            print(c.text)
            found = True


def getRam(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n6"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            print(c.text)
            found = True


def getSSD(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n7"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            print(c.text)
            found = True


def getAirCooler(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n10"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            print(c.text)
            found = True


def getAIO(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n11"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            print(c.text)
            found = True


def getVGA(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n12"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text and "開麥加贈" not in text:
            print(c.text)
            found = True


def getCase(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n14"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            print(c.text)
            found = True


def getPSU(target):
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n15"})
    candidates = results.select("option")
    found = False
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            print(c.text)
            found = True

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
