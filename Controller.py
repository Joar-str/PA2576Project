from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from os import path
from inspect import currentframe, getfile

class mainApp(MDApp):
    scr3 = ObjectProperty()
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Builder.load_file('login_page.kv'))
        return self.sm

mainApp().run()