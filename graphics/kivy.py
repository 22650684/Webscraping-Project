import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner

from kivymd.color_definitions import colors
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout


class MainApp(App):
    def build(self):
        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "Teal"
        self.title = 'Web based Medical Reviews'
        title = Label(text='Medical Reviews database', font_size=25, pos_hint={'center_x': 0.5, 'center_y': 0})
        the_layout = BoxLayout(orientation='vertical')
        the_layout.add_widget(title)

        searchTagSpinner = Spinner(text="Good Tag",
                            values=("id",
                                    "story",
                                    "time Posted",
                                    "good Tag" ,
                                    "similar Tag",
                                    "improved Tag",
                                    "response Tag",
                                    "feel Tag",
                                    "location Tag"),
                            pos_hint={'center_x': 0.5, 'center_y': 0.2})
        the_layout.add_widget(searchTagSpinner)

        returnTagSpinner = Spinner(text="Return Tag",
                            values=("id",
                                    "story",
                                    "time Posted",
                                    "good Tag" ,
                                    "similar Tag",
                                    "improved Tag",
                                    "response Tag",
                                    "feel Tag",
                                    "location Tag"),
                            pos_hint={'center_x': 0.5, 'center_y': .4})
        the_layout.add_widget(returnTagSpinner)
        button1 = Button(text='Click me!', font_size=20, pos_hint={"center_x": 0.5, "center_y": 0.6})
        button1.bind(on_press=self.on_button_press)

        button2 = Button(text='Second Button... Twist', font_size=20, pos_hint={"center_x": 0.5, "center_y": 0.8})
        button2.bind(on_press=self.on_button_press)

        the_layout.add_widget(button1)
        the_layout.add_widget(button2)

        return the_layout

    def on_button_press(self, instance):
        print("Button has been pressed ")


if __name__ == '__main__':
    app = MainApp()
    app.run()