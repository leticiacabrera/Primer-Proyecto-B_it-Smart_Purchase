from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Window(BoxLayout):
    pass

class Precioproducto(App):
    def build(self):
        return Window()

if __name__=='__main__':
    sa = Precioproducto()
    sa.run()