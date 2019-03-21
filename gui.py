from kivy.app import App
from kivy.uix.label import Label


class MyFirstProgramApp(App):
    def build(self):
        return Label(text='Hello world')


def main():
    MyFirstProgramApp().run()


if __name__ == '__main__':
    main()
