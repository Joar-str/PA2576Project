import mysql.connector as mysql
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.toast import toast
from kivy.uix.boxlayout import BoxLayout

MYSQL_USER =  'root' #USER-NAME
MYSQL_PASS =  '12345678' #MYSQL_PASS
MYSQL_DATABASE = 'appproject'#DATABASE_NAME

connection = mysql.connect(user=MYSQL_USER,
                           passwd=MYSQL_PASS,
                           database=MYSQL_DATABASE,
                           host='127.0.0.1')


cnx = connection.cursor(dictionary=True)
class PopMessages:
    def invalid_input(self):
        toast("Incorrect password or username", duration=2)

    def account_created(self):
        toast("You are now a member of Student Market", duration=2)

    def already_exisiting(self):
        toast("A user with this username exists already", duration=3)
    
    def salesAD_created(self):
        toast("A sales advertisement was sucessfully published", duration=4)
    def salesAD_removed(self):
        toast("A sales advertisement was sucessfully published", duration=4)

class User:
    created_password = StringProperty('')
    created_name = StringProperty('')
    PhoneNr = ObjectProperty()

    def __init__(self, name, password, phonenr):
        self.name = name
        self.password = password
        self.phonenr = phonenr

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_phonenr(self):
        return self.phonenr

    def createUser(self):
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

class adManager:

    created_userID = StringProperty('')
    created_description = StringProperty('')
    created_author = StringProperty('')
    created_category = StringProperty('')
    created_price = ObjectProperty()

    def __init__(self, userID, description, author, category, price):
        self.userID = userID
        self.description = description
        self.author = author
        self.category = category
        self.price = price

    def get_userID(self):
        return self.userID

    def get_description(self):
        return self.description

    def get_author(self):
        return self.author
    
    def get_category(self):
        return self.category

    def get_price(self):
        return self.price

    def createAD(self):
        try:
            
            query = f"SELECT User_id FROM User where email = '{self.userID}'"
            cnx.execute(query)
            record = cnx.fetchone()
            UserID1 = record.get('User_id')
            cnx.execute(f"INSERT INTO Sales_ad(USER_id, description, author, category, price ) Values({UserID1},'{self.description}','{self.author}','{self.category}',{self.price})")
            connection.commit()
            connection.close()
            PopMessages().salesAD_created()

        except:
            connection.close()

    def removeAD(self):
        
        cnx.execute(f"DELETE FROM Sales_ad Where Ad_id =  '{self.adID}';")
        connection.commit()
        PopMessages().salesAD_removed()

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

    def update_profile_info(self,name, new_name, password, phonenr):
        cnx.execute(f"SET SQL_SAFE_UPDATES = 0")
        user_id = f"SELECT USER_ID FROM User WHERE email = '{name}'"
        cnx.execute(user_id)
        result = cnx.fetchone()
        connection.commit()
        print(user_id)
        print(name, new_name, password, phonenr, result.get('USER_ID'))
        update = f"UPDATE  User SET email = '{new_name}', password = '{password}', phoneNr = '{phonenr}' "\
                 f"WHERE USER_ID = {result.get('User_ID')}"
        cnx.execute(update)
        connection.commit()

            
        
        
        
class HomePage(Screen):
    pass
















