from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from main import User, HomePage, adManager, LoginPage, PopMessages
from kivymd.toast import toast
from kivy.uix.boxlayout import BoxLayout


class MainApp(MDApp):

    def build(self):
        self.sm = ScreenManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.sm.add_widget(Builder.load_file('KV/first_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/login_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/createAccount_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/home_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/createSalesAD_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/removeAD_page.kv'))

        return self.sm

    def account_labels(self):
        name = self.sm.get_screen("create_account").ids.created_name.text
        password = self.sm.get_screen("create_account").ids.created_password.text
        phoneNr = self.sm.get_screen("create_account").ids.PhoneNr.text
        User(name, password, phoneNr).createUser()

    def salesAD_publish(self):
        
        userID = self.get_name()
        description = self.sm.get_screen("createSalesAD").ids.created_description.text
        author = self.sm.get_screen("createSalesAD").ids.created_author.text
        category = self.sm.get_screen("createSalesAD").ids.created_category.text
        price = self.sm.get_screen("createSalesAD").ids.created_price.text
        adManager(userID, description, author, category, price).createAD()
        
    def salesAD_remove(self):
        adID = self.sm.get_screen("removeAD").ids.specified_adID.text
        adManager(adID).removeAD()
        

    def reset(self):
        self.sm.get_screen('login').ids.user_password.text = ''
        self.sm.get_screen('login').ids.user_name.text = ''
    
    def get_name(self):
        return self.sm.get_screen("login").ids.user_name.text

    def get_password(self):
        return self.sm.get_screen("login").ids.user_password.text

    def get_phonenr(self):
        return HomePage().get_user_info(self.get_name())

    def login_input(self):
        name = str(self.sm.get_screen("login").ids.user_name.text)
        password = str(self.sm.get_screen("login").ids.user_password.text)
        valid = LoginPage().check_account(name, password)
        
        if valid:
            self.root.current = 'home_page'
            self.sm.get_screen('home_page').ids.profile_name.text = name
            
        else:
            PopMessages().invalid_input()

    def set_user_info(self):
        self.sm.get_screen('home_page').ids.edit_user.text = self.sm.get_screen("login").ids.user_name.text



if __name__ == '__main__':
    MainApp().run()