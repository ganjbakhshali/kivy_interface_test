from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.lang import Builder
# from kivy.uix.floatlayout import FloatLayout

# Builder.load_file('floatLayot.kv')
class MyLayout(BoxLayout):
    pass


class floatLayotApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    floatLayotApp().run()