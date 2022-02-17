import mysql.connector as mysql
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
    t1 = User()
    t1.createUser()

#cnx.execute('''INSERT Into User(email, password, phoneNr) values ('test1@..','123',12345)''')
#cnx.execute('''SELECT * FROM User''')