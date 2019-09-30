import kivy, kivy.app
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols =2 
        self.add_widget(Label(text='Úser Name'))
        self.username = TextInput(MULTILINE=False)
        self.add_widget(Label(name=""))
        
class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__== "__main__":
    MyApp().run()