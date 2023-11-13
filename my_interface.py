from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class MyGridLayout(GridLayout):
    name=ObjectProperty(None)
    lname=ObjectProperty(None)
    phone=ObjectProperty(None)
    # initial
    # def __init__(self, **kwargs):
    #     super(MyGridLayout,self).__init__(**kwargs)
        
    #     # set columns
    #     self.cols=1
    #     self.row_force_default=True
    #     self.row_default_height=120
    #     self.col_force_default=True
    #     self.col_default_width=100
        
    #     # create top_Grid
    #     self.top_grid=GridLayout(
    #         row_force_default=True,
    #         row_default_height=40,
    #         col_force_default=True,
    #         col_default_width=100
            
    #     )
    #     self.top_grid.cols=2
        
    #     # Add widgets
    #     self.top_grid.add_widget(Label(text="Name: " ))
        
    #     self.name=TextInput(multiline=False)
    #     self.top_grid.add_widget(self.name)
        
    #     self.top_grid.add_widget(Label(text="Last Name: "))
        
    #     self.Lname=TextInput(multiline=False )
    #     self.top_grid.add_widget(self.Lname)
        
    #     self.top_grid.add_widget(Label(text="Phone: "))
        
    #     self.Phone=TextInput(multiline=False)
    #     self.top_grid.add_widget(self.Phone)
        
    #     # add the top_Grid to app
    #     self.add_widget(self.top_grid)
        
    #     # create submit Botton
    #     self.submit=Button(text="Submit",
    #                        font_size=32,
    #                        size_hint_y=None,
    #                        size_hint_x=None,
    #                        height=50, #pixcel
    #                        width=200 #pixcel
                                                      
    #                        )
    #     self.submit.bind(on_press=self.press)
    #     self.add_widget(self.submit)
    
    def press(self):
        name=self.name.text
        Lname=self.lname.text
        phone=self.phone.text
        message=f'Hello {name} {Lname} your phone Number is: {phone}'
        # self.add_widget(Label(text=message))
        print(f'Hello {name} {Lname} your phone Number is: {phone}')
        self.name.text=""
        self.lname.text=""
        self.phone.text=""
        
  
    
class Xray_application(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    Xray_application().run()
