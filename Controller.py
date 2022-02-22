from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from main import User
from os import path
from inspect import currentframe, getfile

class mainApp(MDApp):
    created_password = ObjectProperty(None)
    created_name = ObjectProperty(None)
    PhoneNr = ObjectProperty(None)

    def build(self):
        self.sm = ScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.sm.add_widget(Builder.load_file('first_page.kv'))
        self.sm.add_widget(Builder.load_file('login_page.kv'))
        self.sm.add_widget(Builder.load_file('createAccount_page.kv'))

        return self.sm

    def submit_btn(self):
        User(self.sm.created_name.text, self.sm.created_password.text, self.sm.PhoneNr.text)
        User.createUser()


mainApp().run()