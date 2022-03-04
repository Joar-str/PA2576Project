from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from main import User, LoginPage, PopMessages, HomePage, adManager
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
        self.sm.add_widget(Builder.load_file('KV/createSalesAD_page.kv'))
        self.sm.add_widget(Builder.load_file('KV/removeAD_page.kv'))
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
        return self.sm.get_screen("login").ids.user_name.text

    def get_password(self):
        return self.sm.get_screen("login").ids.user_password.text

    def get_phonenr(self):
        return HomePage().get_user_info(self.get_name())

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

    def update_profile(self):
        old_name = self.get_name()
        name = self.sm.get_screen('home_page').ids.edit_user.text
        phoneNr = self.sm.get_screen('home_page').ids.profile_phone.text
        password = self.sm.get_screen('home_page').ids.profile_password.text
        user_id = HomePage().get_user_id(old_name)
        HomePage().update_profile_info(user_id, name, password, phoneNr)

    def login_input(self):
        """Funktion som hanterar login. Samt sätter användarens information på Profil skärmen"""
        old_name = self.get_name()
        valid = LoginPage().check_account(self.get_name(), self.get_password())
        if valid:
            self.root.current = 'home_page'
            self.sm.get_screen('home_page').ids.profile_name.text = old_name
            self.sm.get_screen('home_page').ids.edit_user.text = old_name
            self.sm.get_screen('home_page').ids.profile_phone.text = self.get_phonenr()
            self.sm.get_screen('home_page').ids.profile_password.text = self.get_password()


        else:
            self.reset()
            PopMessages().invalid_input()



if __name__ == '__main__':
    MainApp().run()