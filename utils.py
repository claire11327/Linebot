import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import ImageMessage,ImageSendMessage
#from linebot.models import TemplateMessage,TemplateSendMessage


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

'''    
def reply_template(reply_token,message):
    print("in reply_template") 
    line_bot_api = LineBotApi(channel_access_token)
  
    line_bot_api.reply_message(event.reply_token, message)
    return "OK"
'''
'''
def temp_create_message():
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackAction(
                label='postback',
                display_text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageAction(
                label='message',
                text='message text'
            ),
            URIAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
    return message
'''

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
'''
基隆
台北
桃園
新竹
台中
南投
嘉義
台南
高雄
台東
花蓮
宜蘭
澎湖
金門
連江
屏東
東沙
南沙

'''
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
    




"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
