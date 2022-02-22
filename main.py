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


class User:

    def __init__(self, email, password, phoneNr):
        self.email = email
        self.password = password
        self.phoneNr = phoneNr

    def createUser(self):
        try:
            cnx.execute(f"INSERT INTO User(email, password, phoneNr) Values('{self.email}',"
                        f" '{self.password}', '{self.phoneNr}')")
            connection.commit()
        except:
            print('fel.')
            connection.close()




if __name__ == "__main__":
    pass

