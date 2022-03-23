from unicodedata import category
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from main import User, LoginPage, PopMessages, HomePage, Watchlist, adManager, adImages
from kivymd.uix.list import IconRightWidget, ThreeLineAvatarIconListItem
from kivy.uix.checkbox import CheckBox

class MainApp(MDApp):
    """Klass för själva appen."""
    _current_ad_id = int

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

    def amount_ad(self):
        """Skapar en lista under fliken PROFILE med användarens
        skapade ads och retunerar ID  på det ad man trycker på"""
        try:
            ad_list = HomePage().get_all_ads(HomePage().get_user_id(self.get_name()))
            for i in range(len(ad_list)):
                icon = IconRightWidget(icon='pencil-outline')
                item = ThreeLineAvatarIconListItem(text=f"{ad_list[i].get('Ad_id')}",
                                                secondary_text=f"{ad_list[i].get('headline')}"
                                                , tertiary_text=f"Price: {ad_list[i].get('price')}")
                item.add_widget(icon)
                item.bind(on_press=self.edit_ad_input)
                self.sm.get_screen('home_page').ids.container.add_widget(item)
        except:
            ValueError('ValueError')

    def edit_ad_input(self, instance):
        """Tar ad-ID som inparameter och sätter ADet's samtliga beskrivningar på EDIT-AD sidan"""
        ad_id = instance.text
        ad = HomePage().get_specific_ad(ad_id)
        self.sm.get_screen('home_page').ids.edit_headline.text = ad.get('headline')
        self.sm.get_screen("home_page").ids.edit_description.text = ad.get('description')
        self.sm.get_screen("home_page").ids.edit_author.text = ad.get('author')
        self.sm.get_screen("home_page").ids.edit_category.text = ad.get('category')
        self.sm.get_screen("home_page").ids.edit_price.text = str(ad.get('price'))
        self._current_ad_id = ad_id

    def update_ad_input(self):
        """Uppdaterar den nya AD-beskrivningen och skickar argumenten till salesAD_updated"""
        ad_id = self._current_ad_id
        headline = self.sm.get_screen('home_page').ids.edit_headline.text
        dscrp = self.sm.get_screen("home_page").ids.edit_description.text
        author = self.sm.get_screen("home_page").ids.edit_author.text
        cat = self.sm.get_screen("home_page").ids.edit_category.text
        price = self.sm.get_screen("home_page").ids.edit_price.text
        HomePage().update_ad(headline, dscrp, author, cat, price, ad_id)
        PopMessages().salesAD_updated()

    def clear_your_adlist(self):
        """Nollställer AD-listan"""
        self.sm.get_screen('home_page').ids.container.clear_widgets()

    def reset(self):
        """reset funktion som nollställer önskade textFields"""
        self.sm.get_screen('login').ids.user_password.text = ''
        self.sm.get_screen('login').ids.user_name.text = ''

    def get_name(self):
        return self.sm.get_screen("login").ids.user_name.text

    def get_password(self):
        return self.sm.get_screen("login").ids.user_password.text

    def get_phonenr(self):
        return HomePage().get_user_phonenr(self.get_name())

    def salesAD_publish(self):
        """Publiserar en skapad ad och skapar ett objekt från klassen adManager"""

        username = self.get_name()
        headline = self.sm.get_screen("createSalesAD").ids.headline.text
        description = self.sm.get_screen("createSalesAD").ids.created_description.text
        author = self.sm.get_screen("createSalesAD").ids.created_author.text
        category = self.sm.get_screen("createSalesAD").ids.created_category.text
        price = self.sm.get_screen("createSalesAD").ids.created_price.text
        adManager(headline, username, description, author, category, price).createAD()

    def salesAD_remove(self):
        adID = self.sm.get_screen("removeAD").ids.specified_adID.text
        adManager(adID).removeAD()

        
    
    
       
    def watchlist_publish(self):
        """Skapar en bevakningslista från klassen Wachlist"""
    
       
        username = self.get_name()
        category = self.sm.get_screen("home_page").ids.category.text
        headline = self.sm.get_screen("home_page").ids.book_name.text
        author = self.sm.get_screen("home_page").ids.subtype.text
        
        
        Watchlist( username, category, headline, author).create_watchlist()


    def update_profile(self):
        """Funktion som skickar den nya profil informationen till update_profile_info som sedan updaterar databasen"""
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