from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView


class ImageViewerLayout(BoxLayout):
    def load_image(self):
        selected_file = self.ids.file_chooser.selection and self.ids.file_chooser.selection[0]

        if selected_file:
            self.ids.image_widget.source = selected_file


class ImageViewerApp(App):
    def build(self):
        return ImageViewerLayout()


if __name__ == '__main__':
    ImageViewerApp().run()
