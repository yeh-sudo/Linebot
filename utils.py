import os
from urllib import parse

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction, PostbackAction, MessageAction, CarouselColumn

import requests
from bs4 import BeautifulSoup

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

coolpc_url = 'https://www.coolpc.com.tw/evaluate.php'


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def push_message(id, message):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(id, TextSendMessage(text=message))

    return "OK"


def searchKeyword(reply_token):
    reply = reply = "search CPU: type to search cpu\n"\
        "search Motherboard: type to search motherboard\n"\
        "search Ram: type to search to search ram\n"\
        "search SSD: type to search ssd\n"\
        "search Air Cooler: type to search air cooler\n"\
        "search AIO: type to search AIO\n"\
        "search VGA: type to search VGA\n"\
        "search Case: type to search case\n"\
        "search PSU: type to search PSU\n"
    send_text_message(reply_token, reply)

    return "OK"


def getMultiCPU(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("searching CPU...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    # search AMD CPU
    AMDResults = soup.find("optgroup", label="AMD AM5 7000系列")
    for result in AMDResults:
        text = result.text
        if "AMD" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))

    # search Intel CPU
    IntelResults = soup.find("optgroup", label="Intel Raptor Lake-s 13代1700 腳位『適700系列或兼容600系列主板』")
    for result in IntelResults:
        text = result.text
        if "Intel" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))
            print(text)
    
    return "OK"


def getMultiMB(id):
    line_bot_api = LineBotApi(channel_access_token)
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
            line_bot_api.push_message(id, TextSendMessage(text=text))

    return "OK"


def getMultiRam(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("search Ram...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    DDR5Results = soup.find("optgroup", label="桌上型記憶體 DDR5 雙通道")
    for result in DDR5Results:
        text = result.text
        if "DDR5" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))
    
    return "OK"


def getMultiSSD(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("search SSD...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    SSDResults = soup.find("optgroup", label="M.2 PCIe 4.0 (Gen4) SSD固態硬碟")
    for result in SSDResults:
        text = result.text
        if "Gen4" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))
    
    return "OK"


def getMultiAirCooler(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("search Air Cooler...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    AirCoolerResults = soup.find("optgroup", label="Noctua 貓頭鷹 散熱器 【6年保固】")
    for result in AirCoolerResults:
        text = result.text
        if "貓頭鷹" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))
    
    return "OK"


def getMultiAIO(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("search AIO...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    AIOResults = soup.find("optgroup", label="恩傑 NZXT【立光代理 6年保固換新】")
    for result in AIOResults:
        text = result.text
        if "Kraken" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))

    return "OK"


def getMultiVGA(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("search VGA...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    RTX4080Results = soup.find("optgroup", label="NVIDIA RTX4080-16G")
    for result in RTX4080Results:
        text = result.text
        if "MHz" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))

    RTX4090Results = soup.find("optgroup", label="NVIDIA RTX4090")
    for result in RTX4090Results:
        text = result.text
        if "MHz" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))
    
    return "OK"


def getMultiCase(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("search Case...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    LianLiResults = soup.find("optgroup", label="聯力工業 LANLI 機殼")
    for result in LianLiResults:
        text = result.text
        if "聯力" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))
    
    return "OK"


def getMultiPSU(id):
    line_bot_api = LineBotApi(channel_access_token)
    print("search PSU...")
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    PSUResults = soup.find("optgroup", label="華碩 ASUS【0800到府收送】")
    for result in PSUResults:
        text = result.text
        if "華碩" in text:
            line_bot_api.push_message(id, TextSendMessage(text=text))
    
    return "OK"


def getCPU(reply_token, target):
    thumbnail_intel = 'https://www.intel.com.tw/etc.clientlibs/settings/wcm/designs/intel/us/en/images/resources/printlogo.png'
    thumbnail_amd = 'https://s4.itho.me/sites/default/files/styles/picture_size_large/public/amd_v2_82.jpg?itok=6ylKFbG2'
    line_bot_api = LineBotApi(channel_access_token)
    print("searching " + target + "...")
    target = target.lower()
    resp = requests.get(coolpc_url)
    soup = BeautifulSoup(resp.text, "html5lib")

    results = soup.find("select", attrs={"name": "n4"})
    candidates = results.select("option")
    for c in candidates:
        text = c.text
        text = text.lower()
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text:
            if target[0] == 'i' and target[len(target)-1] == 'k' and "kf" in text:
                continue
            moreInfo_url = 'https://coolpc.com.tw/tw/?s=' + target.replace(" ", "+")
            thumbnail_imgUrl = thumbnail_amd
            if target[0] == 'i':
                thumbnail_imgUrl = thumbnail_intel
            textArr = text.split(" ")
            for i in range(len(textArr)):
                if textArr[i][0] == '$':
                    text = textArr[i]
                    break
            buttons_template_message = TemplateSendMessage(
                alt_text=target,
                template=ButtonsTemplate(
                    thumbnail_image_url=thumbnail_imgUrl,
                    title=target,
                    text=text,
                    actions=[
                        URIAction(
                            label='More Info',
                            uri=moreInfo_url
                        )
                    ]
                )
            )
            line_bot_api.reply_message(reply_token, buttons_template_message)
            return "OK"
    
    line_bot_api.reply_message(reply_token, TextSendMessage(text="Invalid product name."))
    return "OK"


def getMB(id, reply_token, target):
    line_bot_api = LineBotApi(channel_access_token)
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
            textArr = text.split("(")
            if len(textArr[0]) >= 40:
                continue
            search = ""
            if is_contains_chinese(target):
                search = parse.quote(target)
            else:
                search = target.replace(" ", "+")
            moreInfo_url = 'https://coolpc.com.tw/tw/?s=' + search
            text = text.split(" ")
            productText = ""
            for i in range(len(text)):
                if text[i][0] == '$':
                    productText = text[i]
                    break
            buttons_template_message = TemplateSendMessage(
                alt_text=target,
                template=ButtonsTemplate(
                    thumbnail_image_url="https://cdn-icons-png.flaticon.com/512/683/683329.png",
                    title=textArr[0],
                    text=productText,
                    actions=[
                        URIAction(
                            label='More Info',
                            uri=moreInfo_url
                        )
                    ]
                )
            )
            line_bot_api.push_message(id, buttons_template_message)
            found = True
            print(c.text)
    if not found:
        line_bot_api.push_message(id, TextSendMessage(text="Invalid product name."))
    return "OK"


def getRam(id, reply_token, target):
    line_bot_api = LineBotApi(channel_access_token)
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
            line_bot_api.push_message(id, TextSendMessage(text=c.text))
            found = True
    if not found:
        line_bot_api.push_message(id, TextSendMessage(text="Invalid product name."))
    return "OK"


def getSSD(id, reply_token, target):
    line_bot_api = LineBotApi(channel_access_token)
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
            line_bot_api.push_message(id, TextSendMessage(text=c.text))
            found = True
    if not found:
        line_bot_api.push_message(id, TextSendMessage(text="Invalid product name."))
    return "OK"


def getAirCooler(id, reply_token, target):
    line_bot_api = LineBotApi(channel_access_token)
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
            line_bot_api.push_message(id, TextSendMessage(text=c.text))
            found = True
    if not found:
        line_bot_api.push_message(id, TextMessage(text="Invalid product name."))
    return "OK"


def getAIO(id, reply_token, target):
    line_bot_api = LineBotApi(channel_access_token)
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
            line_bot_api.push_message(id, TextSendMessage(text=c.text))
            found = True
    if not found:
        line_bot_api.push_message(id, TextMessage(text="Invalid product name."))
    return "OK"


def getVGA(id, reply_token, target):
    thumbnail_nvidia = 'https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/02-nvidia-logo-color-blk-500x200-4c25-p@2x.png'
    thumbnail_amd = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/AMD_Radeon_graphics_logo_2016.svg/1200px-AMD_Radeon_graphics_logo_2016.svg.png'
    line_bot_api = LineBotApi(channel_access_token)
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
        if target in text and "送" not in text and "活動" not in text and "狂" not in text and "購買" not in text and "獨家專案" not in text and "愛加購" not in text and "開賣加贈" not in text:
            if target[len(target)-1] == '0' and "ti" in text:
                continue
            textArr = text.split("(")
            if len(textArr[0]) >= 40:
                continue
            search = ""
            if is_contains_chinese(target):
                search = parse.quote(target)
            else:
                search = target.replace(" ", "+")
            moreInfo_url = 'https://coolpc.com.tw/tw/?s=' + search
            text = text.split(" ")
            productText = ""
            for i in range(len(text)):
                if text[i][0] == '$':
                    productText = text[i]
                    break
            thumbnail_imgUrl = thumbnail_nvidia
            if "rx" in target:
                thumbnail_imgUrl = thumbnail_amd
            buttons_template_message = TemplateSendMessage(
                alt_text=target,
                template=ButtonsTemplate(
                    thumbnail_image_url=thumbnail_imgUrl,
                    title=textArr[0],
                    text=productText,
                    actions=[
                        URIAction(
                            label='More Info',
                            uri=moreInfo_url
                        )
                    ]
                )
            )
            line_bot_api.push_message(id, buttons_template_message)
            found = True
    if not found:
        line_bot_api.push_message(id, TextSendMessage(text="Invalid product name."))
    return "OK"


def getCase(id, reply_token, target):
    line_bot_api = LineBotApi(channel_access_token)
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
            textArr = text.split("/")
            textArr = textArr[0].split(" ")
            title = ""
            for i in range(len(textArr)-1):
                title += textArr[i]
                title += " "
            if len(title) >= 40:
                continue
            search = ""
            if is_contains_chinese(target):
                search = parse.quote(target)
            else:
                search = target.replace(" ", "+")
            moreInfo_url = 'https://coolpc.com.tw/tw/?s=' + search
            text = text.split(" ")
            productText = ""
            for i in range(len(text)):
                if text[i][0] == '$':
                    productText = text[i]
                    break
            buttons_template_message = TemplateSendMessage(
                alt_text=target,
                template=ButtonsTemplate(
                    thumbnail_image_url="https://us.123rf.com/450wm/tanyastock/tanyastock1509/tanyastock150900754/44897374-computer-server-icon.-pc-case-or-tower-sign.-blue-flat-circle-button-with-shadow.-vector.jpg",
                    title=title,
                    text=productText,
                    actions=[
                        URIAction(
                            label='More Info',
                            uri=moreInfo_url
                        )
                    ]
                )
            )
            line_bot_api.push_message(id, buttons_template_message)
            found = True
    if not found:
        line_bot_api.push_message(id, TextSendMessage(text="Invalid product name."))
    return "OK"


def getPSU(id, reply_token, target):
    line_bot_api = LineBotApi(channel_access_token)
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
            line_bot_api.push_message(id, TextSendMessage(text=c.text))
            found = True
    if not found:
        line_bot_api.push_message(id, TextMessage(text="Invalid product name."))
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
