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


class adManager:


    def __init__(self, headline, username, description, author, category, price):
        self.username = username
        self.description = description
        self.author = author
        self.category = category
        self.price = price
        self.headline = headline


    def get_headline(self):
        return self.headline

    def get_description(self):
        return self.description

    def get_author(self):
        return self.author

    def get_category(self):
        return self.category

    def get_price(self):
        return self.price

    def get_userid_ad_list(self):
        user_id = HomePage().get_user_id(self.username)
        return user_id

    def createAD(self):
        try:
            user_id = HomePage().get_user_id(self.username)
            cnx.execute(
                f"INSERT INTO Sales_ad(headline, USER_id, description, author, category, price ) "
                f"Values('{self.headline}',{user_id},'{self.description}',"
                f"'{self.author}','{self.category}',{self.price})")
            connection.commit()
            PopMessages().salesAD_created()

        except:
            connection.close()

    def removeAD(self, id):

        cnx.execute(f"DELETE FROM Sales_ad Where Ad_id =  '{self.adID}';")
        connection.commit()
        PopMessages().salesAD_removed()


class HomePage(Screen):

    def get_user_phonenr(self, email):
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

    def get_ad_info(self, user_id):
        ad_info = f"SELECT headline, description, price FROM Sales_ad WHERE USER_ID = '{user_id}'"
        cnx.execute(ad_info)
        result = cnx.fetchall()
        connection.commit()
        print(result)
        return result

    def count_ads(self, userid):
        count = f"SELECT COUNT(*) from sales_ad where user_id = {userid}"
        cnx.execute(count)
        count_result = cnx.fetchone()
        connection.commit()
        return count_result

    def update_profile_info(self,ID, new_name, password, phonenr):
        cnx.execute(f"SET SQL_SAFE_UPDATES = 0")
        update = f"UPDATE  User SET email = '{new_name}', password = '{password}', phoneNr = {phonenr} "\
                 f"WHERE USER_ID = {ID}"
        cnx.execute(update)
        connection.commit()
        print(ID, new_name, password, phonenr)















