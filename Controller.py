from kivymd.app import MDApp
import mysql.connector as mysql
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from main import User, LoginPage
from kivy.properties import ObjectProperty, StringProperty
from os import path
from inspect import currentframe, getfile

MYSQL_USER =  'root' #USER-NAME
MYSQL_PASS =  'Strandberg13' #MYSQL_PASS
MYSQL_DATABASE = 'appproject'#DATABASE_NAME

connection = mysql.connect(user=MYSQL_USER,
                           passwd=MYSQL_PASS,
                           database=MYSQL_DATABASE,
                           host='127.0.0.1')


cnx = connection.cursor(dictionary=True)



class mainApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.sm.add_widget(Builder.load_file('first_page.kv'))
        self.sm.add_widget(Builder.load_file('login_page.kv'))
        self.sm.add_widget(Builder.load_file('createAccount_page.kv'))
        self.sm.add_widget(Builder.load_file('home_page.kv'))
        return self.sm

    def account_labels(self):
        name = self.sm.get_screen("create_account").ids.created_name.text
        password = self.sm.get_screen("create_account").ids.created_password.text
        phoneNr = self.sm.get_screen("create_account").ids.PhoneNr.text
        User(name, password, phoneNr).createUser()

    def login_input(self):
        name = self.sm.get_screen("login").ids.user_name.text
        password = self.sm.get_screen("login").ids.user_password.text
        LoginPage().check_account(name, password)





if __name__ == '__main__':
    mainApp().run()