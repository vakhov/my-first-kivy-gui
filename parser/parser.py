from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('kivy', 'exit_on_escape', True)


class Kernel:
    text_result: TextInput
    is_user_agent: Switch
    is_tor_proxies: Switch
    tag: TextInput
    attribute: TextInput
    text_info: TextInput


class Parse:

    def run_parse(self, param):
        pass

    def save_parse(self, param):
        pass

    def clear(self, param):
        pass


class ParserApp(App, Kernel, Parse):
    test_site: TextInput
    file_name: TextInput

    def build(self):
        self.title = 'Simple Parser'
        root = BoxLayout(orientation='horizontal', padding=5)  # Создаём гавное окно

        # Описание левой половины окна
        left = BoxLayout(orientation='vertical')
        button_run = Button(text='Run in the terminal', size_hint=[1, .07], on_press=self.run_parse)
        left.add_widget(button_run)

        self.test_site = TextInput(
            text='http://', multiline=False,
            font_size=17, size_hint=[1, .07],
            background_color=[1, 1, 1, .7]
        )
        left.add_widget(self.test_site)

        left_grid = GridLayout(size_hint=[1, .07], cols=2)

        self.file_name = TextInput(text='parser.txt', multiline=False, font_size=17)
        left_grid.add_widget(self.file_name)

        button_save = Button(text='Save in the file', on_press=self.save_parse)
        left_grid.add_widget(button_save)
        left.add_widget(left_grid)

        self.text_result = TextInput(readonly=True)
        left.add_widget(self.text_result)

        root.add_widget(left)
        # Описание правой половины окна

        right = BoxLayout(orientation='vertical', size_hint=[.5, 1])

        is_user_agent_label = Label(text=':: User-agent ::', font_size=16)
        is_proxy_label = Label(text=':: Tor-proxies ::', font_size=16)

        self.is_user_agent = Switch(size_hint=[1, .33], active=True)
        self.is_tor_proxies = Switch(size_hint=[1, .33], active=True)

        right_grid = GridLayout(size_hint=[1, .22], cols=2)
        right_grid.add_widget(is_user_agent_label)
        right_grid.add_widget(self.is_user_agent)
        right_grid.add_widget(is_proxy_label)
        right_grid.add_widget(self.is_tor_proxies)

        self.tag = TextInput(text='', multiline=False, hint_text='Tag', font_size='17')
        self.attribute = TextInput(text='', multiline=False, hint_text='Attribute', font_size=17)

        right_grid.add_widget(self.tag)
        right_grid.add_widget(self.attribute)
        right.add_widget(right_grid)

        self.text_info = TextInput(readonly=True, background_color=[1, 1, 1, .7])
        right.add_widget(self.text_info)

        button_clear = Button(text="Clear", size_hint=[1, .055], on_press=self.clear)
        right.add_widget(button_clear)

        root.add_widget(right)

        return root


if __name__ == '__main__':
    ParserApp().run()
