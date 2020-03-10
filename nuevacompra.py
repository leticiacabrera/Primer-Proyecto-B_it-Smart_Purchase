from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class SigninWindow(BoxLayout):
    pass

class Nuevacompra(App):
    def build(self):
        return SigninWindow()

if __name__=='__main__':
    sa = Nuevacompra()
    sa.run()