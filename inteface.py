from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Line

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # First Row
        self.add_widget(Label(text='Column 1', size_hint_x=0.6))
        self.add_widget(Label(text='Column 2', size_hint_x=0.4))

        # Line Separator
        self.add_separator()

        # Second Row
        self.add_widget(Label(text='Column 1', size_hint_x=0.6))
        self.add_widget(Label(text='Column 2', size_hint_x=0.4))

    def add_separator(self):
        # Add a line as a separator
        with self.canvas:
            Color(0, 0, 0, 1)  # Black color
            Line(points=[self.x, self.top - 50, self.right, self.top - 50], width=2)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
