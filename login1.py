
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class SigninWindow(BoxLayout):

    stringProperty_pwd_field = StringProperty('Contraseña')
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '' :
            info.text = '[color=#FF0000]Se requiere usuario y/o contraseña[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00]Se ha logueado satisfactoriamente!!![/color]'
            else:
                info.text = '[color=#FF0000]Usuario y/o contraseña incorrectas[/color]'

class Login1(App):
    def build(self):
        return SigninWindow()

if __name__=='__main__':
    sa = Login1()
    sa.run()

#https://www.youtube.com/watch?v=fqMO6Dq01A4