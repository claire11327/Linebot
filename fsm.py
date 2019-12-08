from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import reply_image
#from utils import reply_template
from utils import get_location
from utils import get_weather
from utils import get_HD_Rader
#from utils import temp_create_message



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)


    # is going to ##state
    def is_going_to_now_weather(self, event):
        text = event.message.text
        return text == "目前天氣"

    def is_going_to_weather_location(self, event):
        text = event.message.text
        reply_token = event.reply_token
        Location = get_location()
        if text in Location:
            Location_id = Location.index(text)
            print("Location_id: ",Location_id)
            send_text_message(reply_token,"查詢"+text)
            return True
        else:
            send_text_message(reply_token,"無此資料")
            return False
        

    def is_going_to_weather_forcast(self, event):
        text = event.message.text
        return text == "天氣預報"

    def is_going_to_HD_Rader(self, event):
        text = event.message.text
        return text == "雷波圖"

    # on enter / exit ##state
    def on_enter_now_weather(self, event):
        print("I'm entering now_weather") 
        reply_token = event.reply_token
        text = "請問你要查詢哪個位置？\n"  #template
        send_text_message(reply_token,text)

    def on_exit_now_weather(self):
        print("Leaving now_weather")



    def on_enter_weather_location(self, event):
        print("I'm entering weather_location") 
        reply_token = event.reply_token
        Temp = get_weather()
        text = Temp[Location_id]
        send_text_message(reply_token, text)
        self.go_back()

    def on_exit_weather_location(self):
        print("Leaving weather_location")




    def on_enter_weather_forcast(self, event):
        print("I'm entering weather_forcast")
        reply_token = event.reply_token
        #message = temp_create_message()
        #reply_template(reply_token,message)
        #send_text_message(reply_token, text)
        send_text_message(reply_token, "text")
        self.go_back()

    def on_exit_weather_forcast(self):
        print("Leaving weather_forcast")

    def on_enter_HD_Rader(self, event):
        print("I'm entering HD_Rader") 
        reply_token = event.reply_token   
        message = get_HD_Rader()
        reply_image(reply_token,message)
        self.go_back()

    def on_exit_HD_Rader(self):
        print("Leaving HD_Rader")

