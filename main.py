import mysql.connector as mysql
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.toast import toast

from kivy.uix.boxlayout import BoxLayout

MYSQL_USER =  'root' #USER-NAME
MYSQL_PASS =  'Strandberg13' #MYSQL_PASS
MYSQL_DATABASE = 'appproject'#DATABASE_NAME

connection = mysql.connect(user=MYSQL_USER,
                           passwd=MYSQL_PASS,
                           database=MYSQL_DATABASE,
                           host='127.0.0.1')


cnx = connection.cursor(dictionary=True)
class PopMessages:
    """En klass med som har samtliga pop meddelanden"""
    def invalid_input(self):
        toast("Incorrect password or username", duration=2)

    def account_created(self):
        toast("You are now a member of Student Market", duration=2)

    def already_exisiting(self):
        toast("A user with this username exists already", duration=3)

class User:
    created_password = StringProperty('')
    created_name = StringProperty('')
    PhoneNr = ObjectProperty()

    def __init__(self, name, password, phonenr):
        self.name = name
        self.password = password
        self.phonenr = phonenr

    def createUser(self):
        """Funktion som skapar en användare och lägger till i databasen"""
        try:
            cnx.execute(f"INSERT INTO User(email, password, phoneNr) Values('{self.name}',"
                        f" '{self.password}', '{self.phonenr}')")
            connection.commit()
            PopMessages().account_created()

        except:
            connection.close()
            PopMessages().already_exisiting()


class LoginPage(ScreenManager):

    def check_account(self, name, password):
        """Funktion som kollar ifall användaren finns i databasem. Om inte
        så skickas det ett fel meddelande"""
        try:
            password_variable = f"SELECT password FROM User WHERE email = '{name}'"
            cnx.execute(password_variable)
            password_query = cnx.fetchone()
            connection.commit()
            if password == password_query.get('password'):
                return True

            else:
                return False
        except:
            pass

class HomePage(Screen):
    def get_user_info(self, email):
        try:
            """Funktion som returnerar användarens telefonnummer som en string"""
            user_phonenr = f"SELECT phoneNr FROM User Where email = '{email}'"
            cnx.execute(user_phonenr)
            user_query = cnx.fetchone()
            connection.commit()
            return str(user_query.get('phoneNr'))
        except:
            pass

    def get_user_id(self, name):
        user_id = f"SELECT USER_ID FROM User WHERE email = '{name}'"
        cnx.execute(user_id)
        result = cnx.fetchone()
        connection.commit()
        return result.get('USER_ID')

    def update_profile_info(self,ID, new_name, password, phonenr):
        cnx.execute(f"SET SQL_SAFE_UPDATES = 0")
        update = f"UPDATE  User SET email = '{new_name}', password = '{password}', phoneNr = {phonenr} "\
                 f"WHERE USER_ID = {ID}"
        cnx.execute(update)
        connection.commit()
        print(ID, new_name, password, phonenr)















