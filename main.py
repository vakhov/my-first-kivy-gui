from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from random import random

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '400')


class ClickerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = Button(
            text='0',
            font_size=30,
            background_color=[1, 1, 1, 1],
            on_press=self.clicker
        )

    def clicker(self, *args, **kwargs):
        self.button.text = str(int(self.button.text) + 1)
        self.button.background_color = [
            random(),
            random(),
            random(),
            random()
        ]

    def build(self):
        return self.button


if __name__ == '__main__':
    ClickerApp().run()
