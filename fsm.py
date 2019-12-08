from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import reply_image
from utils import get_HD_Rader
from utils import get_location
from utils import get_weather


ID = 0


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_HD_Rader(self, event):
        text = event.message.text
        return text.lower() == "雷波圖"

    def is_going_to_forcast(self, event):
        text = event.message.text
        return text == "天氣預報"


    def is_going_to_weather(self, event):
        text = event.message.text
        if "查詢" in text.lower():
            return True
        else:
            return False

        # return text.lower() == "查詢高鐵時刻表"

    def is_going_to_location(self, event):
        text = event.message.text
        location = get_location()

        if text in location:
            global ID
            ID = location.index(text)
            print("ID = ",ID)
            return True
        else:
            return False
        


 



    def on_enter_HD_Rader(self, event):
        print("I'm entering HD_Rader")

        reply_token = event.reply_token
        message = get_HD_Rader()
        reply_image(reply_token,message)
        self.go_back()

    def on_exit_HD_Rader(self):
        print("Leaving state1")

    
    
    def on_enter_forcast(self, event):
        print("I'm entering weather_forcast")
        reply_token = event.reply_token
        send_text_message(reply_token, "text")
        self.go_back()

    def on_exit_forcast(self):
        print("Leaving forcast")
    




    def on_enter_weather(self, event):
        print("I'm entering weather")

        reply_token = event.reply_token
        message = get_HD_Rader()
        reply_image(reply_token,message)
        # self.go_back()

    def on_exit_weather(self, event):
        print("Leaving weather")


    def on_enter_location(self, event):
        print("I'm entering location")
        reply_token = event.reply_token
        Temp = get_weather()
        temp = Temp[ID]
        print("Temp[",ID,"]=",temp)
        send_text_message(reply_token, temp)
        self.go_back()

    def on_exit_location(self):
        print("Leaving location")




