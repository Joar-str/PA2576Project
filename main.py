import mysql.connector as mysql
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
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
        self.sm.add_widget(Builder.load_file('login_page.kv'))
        return self.sm


class User:
    def __init__(self):
        pass

    def createUser(self):
        self.email = str(input('email:'))
        self.password = str(input('password:'))
        self.phoneNr = int(input('phonenr:'))
        try:
            cnx.execute(f"INSERT INTO User(email, password, phoneNr) Values('{self.email}', '{self.password}', '{self.phoneNr}')")
            connection.commit()
        except:
            print('fel.')
            connection.close()


if __name__ == "__main__":
    pass
    #t1 = User()
    #t1.createUser()

#cnx.execute('''INSERT Into User(email, password, phoneNr) values ('test1@..','123',12345)''')
#cnx.execute('''SELECT * FROM User''')