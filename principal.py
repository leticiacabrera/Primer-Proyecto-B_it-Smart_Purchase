
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    pass

class Principal(App):
    def build(self):
        return SigninWindow()

if __name__=='__main__':
    sa = Principal()
    sa.run()