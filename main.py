import mysql.connector as mysql
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
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


class User:
    created_password = StringProperty('')
    created_name = StringProperty('')
    PhoneNr = ObjectProperty()

    def __init__(self, name, password, phonenr):
        self.name = name
        self.password = password
        self.phonenr = phonenr

    def createUser(self):
        try:
            cnx.execute(f"INSERT INTO User(email, password, phoneNr) Values('{self.name}',"
                        f" '{self.password}', '{self.phonenr}')")
            connection.commit()
        except:
            print('Konto med detta nummer finns redan!')
            connection.close()


class LoginPage:
    def check_account(self, name, password):
        name_variable = cnx(f"SELECT password FROM User WHERE email = f'{name}'")
        connection.commit()
        connection.close()
        valid = False
        if password == name_variable:
            valid = True

        else:
            print('fel lösenord eller användarnamn')

        return valid









