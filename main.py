from kivy.uix.accordion import ListProperty
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.textinput import Texture
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from firebase import firebase
firebase = firebase.FirebaseApplication("https://monitoring-10a0d-default-rtdb.firebaseio.com/", None)
import socket
import random
import sys
from kivy.core.video import Video
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
import requests
from kivymd.uix.dialog import MDDialog
import requests
import platform
import getpass
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
#from kivy.uix.screenmanager.WipeTransition import WipeTransition
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.fitimage import FitImage
import requests
from kivy.loader import Loader
import sys
import os
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.tab import MDTabsBase
from threading import Thread
from kivy.storage.jsonstore import JsonStore
import numpy as np
from kivymd.uix.behaviors import CommonElevationBehavior
from datetime import datetime

store = JsonStore("user_detail.json")

STREAM_URL = "http://127.0.0.1:5000"

KV = """
MDFloatLayout:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "login_screen"

                FitImage:
                    source: "2.jpg"
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
                    pos_hint:{"center_x":.5,"center_y": .5}
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
                    pos_hint: {"center_x":.11,"center_y":.43}
                    color: 1,1,1,1
                    on_active: app.show_password(*args)

                MDLabel:
                    id: password_text
                    text: "Show Password"
                    pos_hint: {"center_x":.64, "center_y":.43}
                    color:1,1,1,1

                MDSpinner:
                    id: spinner
                    size_hint:None,None
                    size: "48dp","48dp"
                    active: False

                HoverButton:
                    text: "Login"
                    text_color:"white"
                    font_size: "18sp"
                    size_hint: .5, .09
                    bold: True
                    pos_hint:{"center_x": .5,"center_y": .3}
                    background_color: 1, 1, 1, 0
                    color: 1,1,1,1
                    canvas.before:
                        Color:
                            rgb: self.background
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [8]
                    on_release:app.login()
                    #on_release: video_stream.start_stream()
            MDScreen:
                name: "block_screen"

                MDLabel:
                    text: "Your Account is Blocked"
                    halign: "center"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    
            
            MDScreen:
                name:"homepage"

                StreamViewer:
                    id: video_stream
                    url: ""

                MDCard:
                    size_hint: None, None
                    pos_hint:{"center_x":.43,"center_y": .93}
                    size_hint: 0.8,.07
                    elevation: 2
                    radius: [25,]
                    border_radius: 4

                    MDIconButton:
                        icon: "server"
                        pos_hint:{"center_x":.1,"center_y":.5}
                        
                    TextInput:
                        id: server
                        hint_text: "Enter Server Url"
                        helper_text: "Please Enter Valid Url"
                        size_hint: .7,None
                        mode: "fill"
                        pos_hint:{"center_x": .45,"center_y": .5}
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
        
                                    
                    MDIconButton:
                        id: clo
                        icon: "magnify"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.clear()

                MDRaisedButton:
                    text: "Start Stream"
                    bold: "True"
                    pos_hint:{"center_x":.9,"center_y":.93}
                    on_release:app.get_url()
                    on_release: video_stream.start_stream()
                    
        
                
<ExtendedButton>
    elevation: 1
    shadow_radius: 12
    -height: "56dp"


<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    unfocus_color: "#fffcf4"





"""



class StreamViewer(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frame = None  # Store frame for updating
        self.running = True  # Flag to stop thread when closing app

    def start_stream(self):
        threading.Thread(target=self.fetch_stream, daemon=True).start()  # Start streaming in a thread
        Clock.schedule_interval(self.update_texture, 1/30)  # Refresh UI at 30 FPS

    def fetch_stream(self):
        """Fetch frames from the Flask stream in a separate thread."""
        print(self.url)
        try:
            resp = requests.get(self.url, stream=True, timeout=5)
            bytes_ = b''
            for chunk in resp.iter_content(chunk_size=4096):
                if not self.running:
                    break
                bytes_ += chunk
                a = bytes_.find(b'\xff\xd8')
                b = bytes_.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = bytes_[a:b+2]
                    bytes_ = bytes_[b+2:]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching stream: {e}")

    def update_texture(self, dt):
        """Update the texture with the latest frame."""
        if self.frame is not None:
            #frame = np.rot90(self.frame)  # Rotate for correct orientation
            h, w = self.frame.shape[:2]
            texture = Texture.create(size=(w, h), colorfmt='rgb')
            texture.blit_buffer(self.frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            self.texture = texture
            self.texture.flip_vertical()

    def on_stop(self):
        """Stop the streaming thread when the app closes."""
        self.running = False

class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):
    '''
    Implements a button of type
    `Extended FAB <https://m3.material.io/components/extended-fab/overview>`_.

    .. rubric::
        Extended FABs help people take primary actions.
        They're wider than FABs to accommodate a text label and larger target
        area.

    This type of buttons is not yet implemented in the standard widget set
    of the KivyMD library, so we will implement it ourselves in this class.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            value = self.height / 4
            self.radius = [value, value, value, value]
            self._radius = value


class abhay(TwoLineAvatarIconListItem):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class HoverButton(Button, HoverBehavior):
    background = ListProperty((71/255, 104/255, 237/255, 1))
    def on_enter(self):
        self.background = (251/255, 104/255, 23/255, 1)
        Animation(size_hint= (.6, .1), d=.3).start(self)

    def on_leave(self):
        self.background = (71/255, 104/255, 237/255, 1)
        Animation(size_hint= (.3, .07), d=.3).start(self)

class HoverButton1(Button, HoverBehavior):
    background = ListProperty((71/255, 104/255, 237/255, 1))
    def on_enter(self):
        self.background = (251/255, 104/255, 23/255, 1)
        

    def on_leave(self):
        self.background = (71/255, 104/255, 237/255, 1)

class Videos(Video):
    pass

class MainApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    last_screen = []
    exit = "0"
    password = ""
    username = "radar"
    url = ""
    
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
    
    def check(self, *args):
        if self.root.ids.server.text == "":
            self.root.ids.clo.icon = ""

        else:
            self.root.ids.clo.icon = "close"

    def get_url(self):
        url = self.root.ids.server.text
        self.root.ids.video_stream.url = url

    def clear(self):
        self.root.ids.server.text = ""
                
    def on_start(self, *args):
        if store.exists("user"):
            pass
        else:
            store.put("user", name=self.username) 
            data = {
                "name":self.username,
                'status':"active"
            }
            #firebase.put(f"chat-app-d2935-default-rtdb/admin/users/account", "name", self.username)
            firebase.post(f"monitoring-10a0d-default-rtdb/admin/users/account", data)
        Clock.schedule_interval(self.check, 0.1)

        try:
            firebase.delete("monitoring-10a0d-default-rtdb/Users/password","")

        except:
            pass
        
        DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
        LOCASE_CHARACTERS = ["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y",'z']
        SYMBOLS = ["@","#","$","%","&","/","?","="]

        COMBINED_List = random.choice(DIGITS) + random.choice(LOCASE_CHARACTERS) +random.choice(SYMBOLS)

        rand_digit = random.choice(DIGITS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        rand_list = random.choice(COMBINED_List)

        rand_digit1 = random.choice(DIGITS)
        rand_lower1 = random.choice(LOCASE_CHARACTERS)
        rand_symbol2 = random.choice(SYMBOLS)
        rand_list2 = random.choice(COMBINED_List)

        temp_pass = rand_digit + rand_lower + rand_symbol + rand_list + rand_digit1 + rand_lower1 + rand_symbol2 + rand_list2

        print(temp_pass)

        data = {
            "password":temp_pass
        }

        firebase.post("monitoring-10a0d-default-rtdb/Users/password", data)
        self.password = temp_pass

        data = firebase.get(f"monitoring-10a0d-default-rtdb/admin/users/account", "")
        for key, value in data.items():
            if value["name"] == self.username:
                print(key)
                time = datetime.now().strftime("%H:%M:%S")
               
                ak = firebase.put(f"monitoring-10a0d-default-rtdb/admin/users/account/{key}", "entry_time", str(time))
                print(ak)

    def check_status(self, *args):
        try:
            data = firebase.get(f"monitoring-10a0d-default-rtdb/admin/users/account", "")

            for user in data.values():
                if user["name"] == self.username:
                    status = user["status"]
                    if status == "active":
                        pass
                    else:
                        self.change_screen("block_screen")
                        toast("Account is Blocked")

        except:
            pass
            
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
            try:
                response = requests.get("https://api64.ipify.org?format=json")
                IPAddr = response.json()["ip"]
            except:
                print("Unable to fetch IP")
            data = {
                "ip_address":IPAddr
            }
            firebase.post("monitoring-10a0d-default-rtdb/admin/users/Threat", data)
            
            self.stop()
        else:
            pass

        
        username = self.root.ids.username.text

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
            try:
                data = firebase.get(f"monitoring-10a0d-default-rtdb/admin/users/account", "")

                for user in data.values():
                    if user["name"] == self.username:
                        status = user["status"]
                        if status == "active":
                            self.change_screen("homepage")
                            toast("login successfully")
                            Clock.schedule_interval(self.check_status, 10)
                        else:
                            self.change_screen("block_screen")
                            toast("Account is Blocked")
                        
                   

            except:
                pass
            #toast("login successfully")
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
