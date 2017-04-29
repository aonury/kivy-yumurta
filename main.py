from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ObjectProperty

import webbrowser


class Anasayfa(Screen):
    """
    Uygulamamizin ana giris ekrani. Kullanicinin karsisina cikan ilk ekranimiz
    bu olacak. Sosyal medya linklerine referans ve uygulamanin diger sayfalar-
    ina erisimi buradan saglayacagiz.
    """
    class SocialMediaLinks(ButtonBehavior, Image):
        """https://github.com/aonury/kivy-yumurta
        Sosyal medya linklerimizi tanimliyoruz. Daha sonra uygulama var ise
        uygulama uzerinden acilacak sekilde konfigure edecegiz.
        """
        def facebook_link(self):
            webbrowser.open("https://www.facebook.com/yumurtamsicak.net/")

        def instagram_link(self):
            webbrowser.open("https://www.instagram.com/yumurtamsicak/")

        def pinterest_link(self):
            webbrowser.open("https://tr.pinterest.com/yumurtamscak/")


class Hakkimizda(Screen):
    pass


class Resimler(Screen):
    pass


class Ekran(ScreenManager):
    """
    Oluşturduğumuz ana ekranları kivy icerisinde kullanabilmek adina once
    main dosyasi icerisinde tanimladik. Hem gorsellik hem de yonetme acisindan
    bize kullanim kolayligi yaratacak.
    """
    hakkimizda = ObjectProperty(None)
    anasayfa = ObjectProperty(None)
    resimler = ObjectProperty(None)


class YumurtaApp(App):
    def build(self):
        sm = Ekran(transition=SlideTransition())
        return sm


if __name__ == '__main__':

    # 2 cesit font kullanacagiz. Regular ve Bold
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')

    # Anasayfa rengimizi beyaz yapiyoruz.
    Window.clearcolor = get_color_from_hex('##FFFFFF')
    YumurtaApp().run()
