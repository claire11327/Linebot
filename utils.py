import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage

import requests
from bs4 import BeautifulSoup

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def reply_image(reply_token,message):
    print("in reply_image") 
    line_bot_api = LineBotApi(channel_access_token)
    # 傳送訊息
    line_bot_api.reply_message(reply_token, message)
    return "OK"


def get_HD_Rader():
    url = 'https://www.cwb.gov.tw/Data/radar/CV1_TW_1000_forPreview.png'
    message = ImageSendMessage(
      original_content_url = url,
      preview_image_url=url
    )
    return message

def get_location():
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    r = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=CWB-64424086-3377-427A-9F8B-4A43176BA7E3")
    res = r.json()
    Record = res["records"]["location"]
    Location = []
    for i in Record:
      Location.append(i["locationName"])
    
    print("Location: ",Location)
    return Location

def get_weather():
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    r = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=CWB-64424086-3377-427A-9F8B-4A43176BA7E3")
    res = r.json()
    Record = res["records"]["location"]
    Temp = []
    for i in Record:
      Temp.append(i["weatherElement"][3]["elementValue"])
    print("Temp: ",Temp)
    return Temp
    


