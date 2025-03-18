


from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from firebase import firebase
firebase = firebase.FirebaseApplication("https://monitoring-10a0d-default-rtdb.firebaseio.com/", None)
import random
import sys
from kivy.core.video import Video
from kivy.app import App
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
import requests
from collections import Counter
from kivymd.uix.dialog import MDDialog

from PIL import Image
import time
from kivy.uix.image import Image, AsyncImage, CoreImage
from kivymd.toast import toast
import random

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatIconButton, MDIconButton, MDFlatButton, MDFloatingActionButton, MDTextButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager,FadeTransition
from kivy.clock import Clock
from kivy.uix.label import Label
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.taptargetview import MDTapTargetView
import threading
import getpass
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.video import Video
from kivy.uix.behaviors import ButtonBehavior
from kivy.factory import Factory
from kivy.uix.button import Button
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.behaviors import TouchBehavior
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.filemanager import MDFileManager
from kivy.core.text import LabelBase
from kivymd.uix.list import IRightBodyTouch,MDList, ThreeLineAvatarIconListItem,ThreeLineAvatarListItem,ImageLeftWidget,ThreeLineIconListItem,OneLineListItem,OneLineAvatarIconListItem,TwoLineAvatarIconListItem,IconLeftWidget, TwoLineAvatarListItem, OneLineAvatarListItem
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.spinner import MDSpinner
from kivy.network.urlrequest import UrlRequest
import os
import platform
from PIL import Image as PILimage
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
import time
from kivymd.uix.bottomsheet import MDListBottomSheet
#from kvdroid.tools.audio import Player
from kivymd.uix.pickers import MDTimePicker
from kivy.graphics.texture import Texture
from kivymd.uix.label import MDIcon
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
#from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.fitimage import FitImage
import requests
import sys
import os
from kivymd.uix.tab import MDTabsBase

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import requests
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.properties import StringProperty
from kivymd.uix.navigationrail import MDNavigationRailItem

store = JsonStore("user_detail.json")

KV = """
MDFloatLayout:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "login_screen"

                FitImage:
                    source: "3.jpg"
                    size:1,1

                MDLabel:
                    text: "Welcome To Smart Monitoring"
                    bold: True
                    color:1,1,1,1
                    font_style: "H4"
                    halign: "center"
                    pos_hint: {"center_x": 0.5, "center_y": 0.92}
                    italic: True

                MDCard:
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .6}
                    size_hint: 0.8,0.06
                    opacity: 0.8
                    elevation: 5
                    radius: [10,]
                    border_radius: 10

                    MDIcon:
                        icon: "account"
                        pos_hint: {"center_x":.65,"center_y":.5}
                            
                    TextInput:
                        id: username
                        hint_text: "Enter Username"
                        hint_text_color:"red"
                        helper_text: "Enter Valid Username"
                        size_hint: .9,None
                        pos_hint:{"center_x": .2,"center_y": .5}
                        height: self.minimum_height
                        multiline: False
                        cursor_color: 0,0,0,1
                        cursor_width:"2sp"
                        background_color: 0,0,0,0
                        padding: 15
                        font_size: "18sp" 
                        normal_color: app.theme_cls.bg_light
                        color_active: app.theme_cls.bg_light
                        icon_left: "magnify"
                        foreground_color: app.theme_cls.secondary_text_color

                MDCard:
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .52}
                    size_hint: 0.8,0.06
                    elevation: 3
                    radius: [10,]
                    opacity: 0.8
                    border_radius: 10
                            
                    MDIcon:
                        icon: "lock"
                        pos_hint: {"center_x":.65,"center_y":.5}
                    
                    TextInput:
                        id: password
                        hint_text: "Enter Password"
                        hint_text_color:"red"
                        helper_text: "Enter Valid Password"
                        password: True
                        size_hint: .9,None
                        pos_hint:{"center_x": .2,"center_y": .5}
                        height: self.minimum_height
                        multiline: False
                        cursor_color: 0,0,0,1
                        cursor_width:"2sp"
                        background_color: 0,0,0,0
                        padding: 15
                        font_size: "18sp" 
                        normal_color: app.theme_cls.bg_light
                        color_active: app.theme_cls.bg_light
                        icon_left: "magnify"
                        foreground_color: app.theme_cls.secondary_text_color

            
                MDCheckbox:
                    id:check
                    size_hint: None, None
                    size: "48dp","48dp"
                    pos_hint: {"center_x":.11,"center_y":.46}
                    color: 1,1,1,1
                    on_active: app.show_password(*args)

                MDLabel:
                    id: password_text
                    text: "Show Password"
                    pos_hint: {"center_x":.64, "center_y":.46}
                    color:1,1,1,1

                MDSpinner:
                    id: spinner
                    size_hint:None,None
                    size: "48dp","48dp"
                    active: False

                MDRaisedButton:
                    text: "Login"
                    theme_text_color: "Custom"
                    
                    text_color:"white"
                    font_size: "18sp"
                    size_hint: .5, .07
                    bold: True
                    pos_hint:{"center_x": .5,"center_y": .4}
                    md_bg_color:1,0,0,1
                    
                    
                    on_release:app.login()

            
            MDScreen:
                name:"homepage"

                ScrollView:
                    size_hint:1,1
                    bar_width:0
                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: "1500dp"
                        #spacing: dp(10)
                        #padding: dp(10)

                        MDFloatLayout:
                            MDFloatLayout:
                                md_bg_color: 0,0,1,1
                                size_hint:1,.1
                                pos_hint:{"center_x":.5,"center_y":.95}

                            MDLabel:
                                text:"Admin Panel"
                                bold:True
                                font_size: "20sp"
                                pos_hint:{"center_x":.52,"center_y":.98}

                            Hovercard:
                                size_hint: None, None
                                pos_hint:{"center_x":.25,"center_y": .9}
                                size_hint: 0.42,.1
                                elevation: 2
                                radius: [15,]
                                border_radius: 4

                                MDRelativeLayout:
                                    MDLabel:
                                        text: "Total Users"
                                        bold: True
                                        halign: "center"
                                        font_size: "23sp"
                                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1

                                    MDLabel:
                                        id: users
                                        text: "10"
                                        bold: True
                                        halign: "center"
                                        font_size: "30sp"
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1


                            Hovercard:
                                size_hint: None, None
                                pos_hint:{"center_x":.75,"center_y": .9}
                                size_hint: 0.42,.1
                                elevation: 2
                                radius: [15,]
                                border_radius: 4

                                MDRelativeLayout:

                                    MDLabel:
                                        text: "Active Users"
                                        bold: True
                                        halign: "center"
                                        font_size: "23sp"
                                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1

                                    MDLabel:
                                        id: active
                                        bold: True
                                        halign: "center"
                                        font_size: "30sp"
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1

                            Hovercard:
                                size_hint: None, None
                                pos_hint:{"center_x":.25,"center_y": .79}
                                size_hint: 0.42,.1
                                elevation: 2
                                radius: [15,]
                                border_radius: 4

                                MDRelativeLayout:

                                    MDLabel:
                                        text: "Blocked Users"
                                        bold: True
                                        halign: "center"
                                        font_size: "23sp"
                                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1

                                    MDLabel:
                                        id: blocked
                                        bold: True
                                        halign: "center"
                                        font_size: "30sp"
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1

                            Hovercard:
                                size_hint: None, None
                                pos_hint:{"center_x":.75,"center_y": .79}
                                size_hint: 0.42,.1
                                elevation: 2
                                radius: [15,]
                                border_radius: 4

                                MDRelativeLayout:

                                    MDLabel:
                                        text: "Threats"
                                        bold: True
                                        halign: "center"
                                        font_size: "23sp"
                                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1

                                    MDLabel:
                                        id: threats
                                        text: "0"
                                        bold: True
                                        halign: "center"
                                        font_size: "30sp"
                                        theme_text_color: "Custom"
                                        text_color: 138/255,242/255,166/255,1

                            
                            MDFloatLayout:
                                MDCard:
                                    size_hint: None, None
                                    pos_hint:{"center_x":.5,"center_y": .62}
                                    size_hint: 0.9,.2
                                    elevation:1
                                    radius: [10,]
                                    border_radius: 2

                                    ScrollView:
                                        size_hint:1,.8
                                        MDBoxLayout:
                                            id: active_users
                                            orientation: "vertical"
                                            size_hint_y: None
                                            height:"320dp"
                                            spacing: dp(10)
                                            padding: dp(10)

                                            

                            MDLabel:
                                text: "Active Users"
                                bold:True
                                pos_hint:{"center_x":.56,"center_y": .7}
                                font_size:"18sp"
                                
                            MDLabel:
                                id:empty_active
                                text: ""
                                bold:True
                                pos_hint:{"center_x":.75,"center_y": .62}
                                font_size:"25sp"
                                
                            MDFloatLayout:
                                MDCard:
                                    size_hint: None, None
                                    pos_hint:{"center_x":.5,"center_y": .39}
                                    size_hint: 0.9,.2
                                    elevation: 1
                                    radius: [10,]
                                    border_radius: 2
                                    
                                        

                                    ScrollView:
                                        size_hint:1,.8
                                        MDBoxLayout:
                                            id: block_list
                                            orientation: "vertical"
                                            size_hint_y: None
                                            height:"320dp"
                                            spacing: dp(10)
                                            padding: dp(10)


                            MDLabel:
                                text: "Blocked Users"
                                bold:True
                                pos_hint:{"center_x":.56,"center_y": .47}
                                font_size:"18sp"
                                
                            MDLabel:
                                id:empty_block
                                text: ""
                                bold:True
                                pos_hint:{"center_x":.75,"center_y": .38}
                                font_size:"25sp"
                                
                            MDFloatLayout:
                                MDCard:
                                    size_hint: None, None
                                    pos_hint:{"center_x":.5,"center_y": .16}
                                    size_hint: 0.9,.2
                                    elevation: 1
                                    radius: [10,]
                                    border_radius: 2

                                    ScrollView:
                                        size_hint:1,.8
                                        MDBoxLayout:
                                            id: threats_list
                                            orientation: "vertical"
                                            size_hint_y: None
                                            height:"320dp"
                                            spacing: dp(10)
                                            padding: dp(10)


                            MDLabel:
                                text: "Threats"
                                bold:True
                                pos_hint:{"center_x":.56,"center_y": .24}
                                font_size:"18sp"                            
                



"""

class Hover1card(MDCard):
    pass

class Hovercard(MDCard):
    pass


class HoverButton(Button):
    pass
    
class HoverButton1(Button):
    pass
    

class Videos(Video):
    pass

class MainApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    last_screen = []
    title = "Smart Monitoring"
    __version__ = "0.7"
    exit = "0"
    password = ""
    username = ""
    dialog = None
    #win_size = min(Window.size)
    
    def build(self):
        screen = Builder.load_string(KV)
        self.theme_cls.accent_palette = self.theme_cls.primary_palette
        return screen
            
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard == 13:
            if self.root.ids.screen_manager.current == 'login_screen':
                self.login()
            else:
                pass
      
        if keyboard in (1001, 27):   
            if self.manager_open:
                self.file_manager.back()
            else:
                self.back_screen()
 
        return True
                
    def on_start(self, *args):
        if store.exists("user"):
            self.stop()
        else:
            self.get()
            self.get_ip()

    def remove_ip(self, n):
        data = firebase.delete(f"monitoring-10a0d-default-rtdb/admin/users/Threat/{n}", "")
        toast("IP Address removed successfully")
        self.get_ip()

    def get(self):
        card_list = self.root.ids.active_users
        card_list.clear_widgets()
        self.root.ids.block_list.clear_widgets()
        data = firebase.get(f"monitoring-10a0d-default-rtdb/admin/users/account", "")
        
        try:
            try:
                for i in range(len(data)):
                    p = int(i)+1
                    self.root.ids.users.text = str(p)
        
                    ak = p*80
                    self.root.ids.active_users.height = str(ak)+"dp"
                    self.root.ids.block_list.height = str(ak)+"dp"
                    
            except:
                pass
    
            data = firebase.get(f"monitoring-10a0d-default-rtdb/admin/users/account", "")
            print(data)
            for key, value in data.items():
                try:
                    name = value["name"]
                    status = value["status"]
                    id = key
                    k = sum(1 for user in data.values() if user["status"] == "active")
                    sl = sum(1 for user in data.values() if user["status"] == "blocked")
                    self.root.ids.active.text = str(k)
                    self.root.ids.blocked.text = str(sl)
                    if status == "active":
                        s = Hover1card(size_hint= (.95, .1), elevation= 1, radius= [10,])
                        w = MDRelativeLayout()
                        a = FitImage(source="https://cdn.pixabay.com/photo/2013/07/12/15/59/proximity-150698_1280.png", size_hint= (.17, .85), pos_hint= {"center_x":.1,"center_y": .5})
                        w.add_widget(a)
                        s.add_widget(w)
                        sd = MDLabel(text=name,pos_hint= {"center_x":.7,"center_y": .7},bold=True,font_size="30sp")
                        sd1 = MDLabel(text=f"Account: {status}",pos_hint= {"center_x":.7,"center_y": .3},font_size="15sp")
                        
                        w.add_widget(sd)
                        w.add_widget(sd1)
                        sf = MDRaisedButton(text="Block User",pos_hint= {"center_x":.8,"center_y": .5})
                        sf.bind(on_release=lambda instance, n=key: self.block_user(n))
                        w.add_widget(sf)
                        card_list.add_widget(s)
                        
                    else:
                        s = Hover1card(size_hint= (.95, .1), elevation= 1, radius= [10,])
                        w = MDRelativeLayout()
                        a = FitImage(source="https://cdn.pixabay.com/photo/2013/07/12/15/59/proximity-150698_1280.png", size_hint= (.17, .85), pos_hint= {"center_x":.1,"center_y": .5})
                        w.add_widget(a)
                        s.add_widget(w)
                        sd = MDLabel(text=name,pos_hint= {"center_x":.7,"center_y": .7},bold=True,font_size="30sp")
                        sd1 = MDLabel(text=f"Account: {status}",pos_hint= {"center_x":.7,"center_y": .3},font_size="15sp")
                        
                        w.add_widget(sd)
                        w.add_widget(sd1)
                        sf = MDRaisedButton(text="Unblock User",pos_hint= {"center_x":.8,"center_y": .5})
                        sf.bind(on_release=lambda instance, n=key: self.unblock_user(n))
                        w.add_widget(sf)
                        self.root.ids.block_list.add_widget(s)
    
                except:
                    pass
                    
        except:
            pass
            
        self.root.ids.empty_active.text = ""
        self.root.ids.empty_block.text = ""
        if self.root.ids.active.text == "0":
            self.root.ids.empty_active.text = "No Active Account"
            print("No User Have Active Account")
            
        elif self.root.ids.blocked.text == "0":
            self.root.ids.empty_block.text = "No User Is Blocked"
            print("No User Is Blocked")
            
        else:
            pass


    def get_ip(self):
        threat_list = self.root.ids.threats_list
        threat_list.clear_widgets()
        data = firebase.get(f"monitoring-10a0d-default-rtdb/admin/users/Threat", "")
        try:
            for i in range(len(data)):
                p = int(i)+1

                ak = p*80
                self.root.ids.threats_list.height = str(ak)+"dp"

        except:
            pass

        data = firebase.get(f"monitoring-10a0d-default-rtdb/admin/users/Threat", "")
        try:
            ip_count = len(data)
            self.root.ids.threats.text = str(ip_count)
            for key, value in data.items():
                name = value["ip_address"]

                s = Hover1card(size_hint= (1, .1), elevation= 1, radius= [10,])
                s.bind(on_release=lambda instance, n=name: self.info(n))
                w = MDRelativeLayout()
                a = FitImage(source="https://cdn.pixabay.com/photo/2013/07/12/15/59/proximity-150698_1280.png", size_hint= (.17, .85), pos_hint= {"center_x":.09,"center_y": .5})
                w.add_widget(a)
                sd = MDLabel(text=f"IP Address",pos_hint= {"center_x":.69,"center_y": .7},bold=True,font_size="30sp")
                sd1 = MDLabel(text=name,pos_hint= {"center_x":.67,"center_y": .3},font_size="30sp")
                w.add_widget(sd)
                w.add_widget(sd1)
                s.add_widget(w)
                sf = MDRaisedButton(text="Remove IP",pos_hint= {"center_x":.85,"center_y": .5})
                sf.bind(on_release=lambda instance, n=key: self.remove_ip(n))
                threat_list.add_widget(s)

        except:
            pass

    def info(self, n):
        response = requests.get(f"http://ip-api.com/json/{n}")
        data = response.json()

        if data["status"] == "success":
            info = {
                "IP Address": data["query"],
                "Country": data["country"],
                "Region": data["regionName"],
                "City": data["city"],
                "Latitude": data["lat"],
                "Longitude": data["lon"],
                "ISP": data["isp"],
                "Organization": data["org"],
                "Time Zone": data["timezone"],
                "ZIP Code": data["zip"],
            }

            print(info)

        else:
            print("Error:Could not retrieve details")


        device_info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Device Name": platform.node(),
            "Username": getpass.getuser(),
            "Processor": platform.processor(),
            "Architecture": platform.architecture()[0]
        }

        print(device_info)

        if not self.dialog:
            self.dialog = MDDialog(
                title="Information",
                text=f"IP Address: {n}\n"
                f"Country: {info['Country']}\n"
                f"Region: {info['Region']}\n"
                f"City: {info['City']}\n"
                f"Latitude: {info['Latitude']}\n"
                f"Longitude: {info['Longitude']}\n"

                f"ISP: {info['ISP']}\n"
                f"Organization: {info['Organization']}\n"
                f"Time Zone: {info['Time Zone']}\n"
                f"ZIP Code: {info['ZIP Code']}\n"

                f"OS: {device_info['OS']}\n"
                f"OS Version: {device_info['OS Version']}\n"
                f"Device Name: {device_info['Device Name']}\n"
                f"Processor: {device_info['Processor']}\n"
                f"Architecture: {device_info['Architecture']}\n"
                f"Username: {device_info['Username']}\n"

                
                
                
                
            )
        self.dialog.open()

    def block_user(self, n):

        data = firebase.put(f"monitoring-10a0d-default-rtdb/admin/users/account/{n}", "status", "blocked")
        toast("User blocked successfully")
        self.get()


    def unblock_user(self, n):
        data = firebase.put(f"monitoring-10a0d-default-rtdb/admin/users/account/{n}", "status", "active")
        toast("User unblocked successfully")
        self.get()

    def back_screen(self, *args):
        if self.root.ids.screen_manager.current != "homepage":
            self.change_screen(self.last_screen[-1], 'right')
            self.last_screen.pop(-1)
            
    def change_screen(self, screen, *args):
        if self.root.ids.screen_manager.current == 'homepage' or self.root.ids.screen_manager.current == "hl":
            try:
                pass
            except:
                pass
        if args:
            self.root.ids.screen_manager.transition.direction = args[0]
            if args[0] != 'right':
                self.last_screen.append(self.root.ids.screen_manager.current)
                
        else:
            self.root.ids.screen_manager.transition.direction = 'left'
            self.last_screen.append(self.root.ids.screen_manager.current)
        self.root.ids.screen_manager.current = screen

    def login(self):
        self.exit += "1"

        if self.exit == "0111":
            toast("Sorry sir you can't access admin panel")
            store.put("user", account="blocked") 
            self.stop()
        else:
            pass

        
        username = self.root.ids.username.text
        res = firebase.get("monitoring-10a0d-default-rtdb/admin_detail", "")

        print(res)
        for i in res.keys():
            print(res[i]["name"])
            print(res[i]["password"])

            self.username = res[i]["name"]
            self.password = res[i]["password"]
        if self.username == username:
            pass
        else:
            self.root.ids.username.text = ""
            self.root.ids.username.hint_text = "Enter Valid Username"
            toast("Wrong Username")

        password = self.root.ids.password.text
            
        if self.password == password:
            pass
        else:
            self.root.ids.password.text = ""
            self.root.ids.password.hint_text = "Enter Valid Password"
            toast("Wrong Password")

        if self.username == username and self.password == password:
            self.change_screen("homepage")
            toast("login successfully")
        else:
            pass

        self.root.ids.spinner.active = False
       
        

    def show_password(self, checkbox, value):
        if value:
            self.root.ids.password.password = False
            self.root.ids.password_text.text = "Hide Password"
        else:
            self.root.ids.password.password = True
            self.root.ids.password_text.text = "Show Password"
        
MainApp().run()
