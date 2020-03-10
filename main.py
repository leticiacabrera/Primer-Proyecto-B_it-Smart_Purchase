from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    spacing: 10
   
    space_x: self.size[1]/10
    canvas:
        Color: 
            rgba: (1,1,1,.8)
        Rectangle: 
            size: self.size
            pos: self.pos
    BoxLayout:
        size_hint_y: None
        height: 50 
        canvas.before:
            Color: 
                rgba: (.06,.45,.45,.7)
            Rectangle: 
                size: self.size
                pos: self.pos
    Label:
        text: 'Camara:'
        color: 0,0,0,1
        size_hint_y: None
        height: 50

    FloatLayout:
        Camera:
            id: camera
            resolution: (640, 480)
            play: False
            size_hint: None, None
            height: 500
            width: 500
            pos_hint: {'center_x': .5, 'y': -.1}
    
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: 40
        background_color: (.06,.45,.45,.7)
        background_normal: ''
    Button:
        text: 'Capture'
        size_hint_y: None
        height: 40
        background_color: (.06,.45,.45,.7)
        background_normal: ''
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%d%m%Y_%H%M%S")
        camera.export_to_png("C:\\Users\\letic\\OneDrive\\Escritorio\\Python\\Practica Kivy\\photo\\IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()