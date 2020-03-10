from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class SigninWindow(BoxLayout):
    stringProperty_pwd_field = StringProperty('Código promoción')

class Listacompras(App):
    def build(self):
        return SigninWindow()

if __name__=='__main__':
    sa = Listacompras()
    sa.run()