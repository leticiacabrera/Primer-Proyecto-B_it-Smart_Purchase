import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class RegistrodeUsuario(BoxLayout):
    pass
        


class RegistrodeusuarioApp(App):
    def build(self):
        return RegistrodeUsuario()

if __name__=='__main__':
    ru = RegistrodeusuarioApp()
    ru.run()