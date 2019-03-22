from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')
Config.set('kivy', 'exit_on_escape', True)

saveInput = ''


class CalculatorApp(App):
    result: TextInput
    symbol_buttons = [
        '7', '8', '9', '+', '<',
        '4', '5', '6', '-', '(',
        '1', '2', '3', '*', ')',
        '0', '.', '=', '/', '%'
    ]

    def calculator(self, symbol):
        global saveInput
        if symbol.text is '<':
            self.result.text = ''
        elif symbol.text is not '=':
            self.result.text += symbol.text
        else:
            try:
                self.result.text = str(eval(self.result.text))
            except (SyntaxError, NameError):
                self.result = ''

    def build(self):
        root = BoxLayout(orientation='vertical', padding=5)
        self.result = TextInput(
            text='', readonly=True, font_size=25,
            size_hint=[1, 0.75], background_color=[1, 1, 1, 0.8]
        )
        root.add_widget(self.result)

        all_button = GridLayout(cols=5)
        for symbol in self.symbol_buttons:
            all_button.add_widget(Button(text=symbol, on_press=self.calculator))
        root.add_widget(all_button)
        return root


if __name__ == '__main__':
    CalculatorApp().run()
