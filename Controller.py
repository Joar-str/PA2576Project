from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from main import User, LoginPage, PopMessages, HomePage
from kivymd.toast import toast
from kivy.uix.boxlayout import BoxLayout


class MainApp(MDApp):
    """Klass för själva appen."""

    def build(self):
        """Build funktion som initierar samtliga filer"""
        self.sm = ScreenManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.sm.add_widget(Builder.load_file('KV/first_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/login_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/createAccount_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/home_page.kv'))
        return self.sm

    def account_labels(self):
        """Skapar ett objekt av klassen User med samtliga inparametrar"""
        name = self.sm.get_screen("create_account").ids.created_name.text
        password = self.sm.get_screen("create_account").ids.created_password.text
        phoneNr = self.sm.get_screen("create_account").ids.PhoneNr.text
        User(name, password, phoneNr).createUser()


    def reset(self):
        """reset funktion som nollställer önskade textFields"""
        self.sm.get_screen('login').ids.user_password.text = ''
        self.sm.get_screen('login').ids.user_name.text = ''

    def get_name(self):
        name = str(self.sm.get_screen("login").ids.user_name.text)
        return name

    def get_password(self):
        password = str(self.sm.get_screen("login").ids.user_password.text)
        return password

    def get_phonenr(self):
        phoneNr = HomePage().get_user_info(self.get_name())
        return phoneNr

    def login_input(self):
        """Funktion som hanterar login. Samt sätter användarens information på Profil skärmen"""
        #name = str(self.sm.get_screen("login").ids.user_name.text)
        #password = str(self.sm.get_screen("login").ids.user_password.text)
        #phoneNr = HomePage().get_user_info(name)
        valid = LoginPage().check_account(self.get_name(), self.get_password())
        if valid:
            self.root.current = 'home_page'
            self.sm.get_screen('home_page').ids.profile_name.text = self.get_name()
            self.sm.get_screen('home_page').ids.edit_user.text = self.get_name()
            self.sm.get_screen('home_page').ids.profile_phone.text = self.get_phonenr()
            self.sm.get_screen('home_page').ids.profile_password.text = self.get_password()
            self.reset()

        else:
            PopMessages().invalid_input()







if __name__ == '__main__':
    MainApp().run()