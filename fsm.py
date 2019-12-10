from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import reply_image
from utils import get_HD_Rader
from utils import get_location
from utils import get_weather
from utils import get_forcast
from utils import get_location_Image


ID = 0
default_ID = 0
loc = ''
using_default = -1


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_HD_Rader(self, event):
        text = event.message.text
        return text.lower() == "雷波圖"


    def is_going_to_menu(self, event):
        text = event.message.text
        if "目錄" in text or "主選單" in text or "教學" in text:
            return True
        return False

    def is_going_to_set_location(self, event):
        text = event.message.text
        location = get_location()
        for i in range(len(location)):
            print("Location[",i,"] is ",location[i])
            if location[i].find(text) != -1:
                global default_ID
                default_ID = i
                print("default_ID = ",default_ID)
                global loc
                loc = location[i]
                return True
        return False



    def is_going_to_search(self, event):
        text = event.message.text
        if "查詢" in text.lower():
            return True
        else:
            return False
            
    def is_going_to_location(self, event):
        text = event.message.text
        if text.lower() == 'y':
            global using_default
            using_default = 1        
            return True
        else:
            text = text.replace("台","臺")
            text = text[0:2]
            location = get_location()
            for i in range(len(location)):
                print("Location[",i,"] is ",location[i])
                if location[i].find(text) != -1:
                    global ID
                    ID = i
                    print("ID = ",ID)
                    return True
            return False
        

    def is_going_to_weather(self, event):
        text = event.message.text
        if "目前" in text:
            return True
        else:
            return False
   

    def is_going_to_forcast(self, event):
        text = event.message.text
        if "預報" in text:
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

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        text = "請輸入\'雷波圖\'：查詢目前雷波圖\n請輸入\'查詢\':查詢天氣\n請輸入\'[城市名]\':設定預設城市"
        send_text_message(reply_token, text)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")


    

    def on_enter_set_location(self, event):
        print("I'm entering set_location")
        reply_token = event.reply_token
        message = get_location_Image(loc)
        reply_image(reply_token,message)
        self.go_back()





    def on_exit_set_location(self):
        print("Leaving set_location")




    def on_enter_search(self, event):
        print("I'm entering search")
        reply_token = event.reply_token
        text = "請輸入查詢的城市,輸入\'y\'：使用預設城市"
        send_text_message(reply_token, text)
        

    def on_exit_search(self, event):
        print("Leaving search")

    def on_enter_location(self, event):
        print("I'm entering location")
        reply_token = event.reply_token
        text = "請輸入\"目前\"：查詢現在天氣，輸入\"預報\":查詢明天天氣"
        send_text_message(reply_token, text)

    def on_exit_location(self,event):
        print("Leaving location")
 
    def on_enter_weather(self, event):
        print("I'm entering weather")
        reply_token = event.reply_token
        text = get_weather()
        global using_default
        if using_default == 1:
            send_text_message(reply_token,text[default_ID])
            print(default_ID)
            using_default = -1
        else:
            send_text_message(reply_token,text[ID])

        self.go_back()

    def on_exit_weather(self):
        print("Leaving forcast")
    
    
    def on_enter_forcast(self, event):
        print("I'm entering weather_forcast")
        reply_token = event.reply_token
        Text = get_forcast()
        if using_default == 1:
            send_text_message(reply_token,Text[default_ID])
        else:
            send_text_message(reply_token,Text[ID])
        self.go_back()

    def on_exit_forcast(self):
        print("Leaving forcast")
    



