from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

# from kivy.uix.floatlayout import FloatLayout

# Builder.load_file('Se15kivy.kv')
class MyLayout(BoxLayout):
    def press(self):
        name=self.ids.text_input.text
        self.ids.name_label.text=f"Hello {name}!"
        self.ids.text_input.text=""
        


class Se15kivyApp(App):
    def build(self):
        # Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    Se15kivyApp().run()