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
    r = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=CWB-64424086-3377-427A-9F8B-4A43176BA7E3")
    res = r.json()
    Record = res["records"]["locations"][0]["location"]
    Location = []
    for i in Record:
      Location.append(i["locationName"])
    
    print("Location: ",Location)
    return Location



def get_weather():
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    r = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=CWB-64424086-3377-427A-9F8B-4A43176BA7E3")
    res = r.json()
    Record = res["records"]["locations"][0]["location"]
    Temp = []
    for i in Record:
      weather = i["weatherElement"][10]["time"][0]["elementValue"][0]["value"]
      temp =  weather.split("。")
      Temp.append(temp[0] + "\n" + temp[1]  + "\n" + temp[2] + "\n" + temp[3])
    print("Temp: ",Temp, "\n")
    return Temp
    


def get_forcast():
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
    r = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=CWB-64424086-3377-427A-9F8B-4A43176BA7E3")
    res = r.json()
    Record = res["records"]["locations"][0]["location"]
    Forcast = []
    for i in Record:
      weather = i["weatherElement"][10]["time"][1]["elementValue"][0]["value"]
      temp = weather.split("。")
      Forcast.append(i["locationName"] +" : \n"+ temp[0] + "\n" + temp[1]+ "\n"  + temp[2]+ "\n" +temp[3])
    print("Forcast: ",Forcast, "\n")
    return Forcast


def get_location_Image(location_input):
    print("location_input",location_input)
    source = [
      "https://imgur.com/apEPRZU.jpg", "https://imgur.com/XMxS4TL.jpg", "https://imgur.com/3y13vNr.jpg", 
      "https://imgur.com/SCRza25.jpg", "https://imgur.com/BoupMaq.jpg", "https://imgur.com/cNo47bJ.jpg",
      "https://imgur.com/HXSrgSE.jpg", "https://imgur.com/ImWCNdF.jpg", "https://imgur.com/luJcfGz.jpg", 
      "https://imgur.com/V6md6Oq.jpg", "https://imgur.com/10CLegx.jpg", "https://imgur.com/t76xmZo.jpg", 
      "https://imgur.com/3ctRyGz.jpg", "https://imgur.com/3wXAmb9.jpg", "https://imgur.com/YKQS5om.jpg", 
      "https://imgur.com/HkAYRJy.jpg", "https://imgur.com/9tE5KKG.jpg", "https://imgur.com/VXSGlag.jpg", 
      "https://imgur.com/jKGnc09.jpg", "https://imgur.com/02wPEkY.jpg", "https://imgur.com/l0x9gGx.jpg", 
      "https://imgur.com/7VaBTCd.jpg", "https://imgur.com/3zlw2Y3.jpg", "https://imgur.com/RmbQV2O.jpg"
    ]

    Image_Location = ["嘉義","臺東","宜蘭","臺南","小琉球","東沙","花蓮","彰化","南投","苗栗","雲林","新北","蘭嶼","臺中","澎湖","桃園","綠島","馬祖","新竹","金門","臺北","屏東","高雄","基隆"]


    url = "https://imgur.com/YCwsT8P.png"
    for i in range(len(source)):
      print("Image_Location[i] = ",Image_Location[i])
      if location_input.find(Image_Location[i]) != -1:
        url = source[i]
    message = ImageSendMessage(
      original_content_url = url,
      preview_image_url=url
    )
    print("url: ",url)
    return message
