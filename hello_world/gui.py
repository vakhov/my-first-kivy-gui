from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyFirstProgramApp(App):
    def build(self):
        return Button(text='Hello world')


def main():
    MyFirstProgramApp().run()


if __name__ == '__main__':
    main()
