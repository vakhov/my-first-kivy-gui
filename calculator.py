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


class CalculatorApp(App):
    """
    Реализация простого калькулятора
    """
    # Хранение строки IO
    result: TextInput
    memory: str

    # Символы кнопок калькулятора
    symbol_buttons = [
        'mr', 'mc', 'm', 'pi', 'AC',
        '7', '8', '9', '+', '<',
        '4', '5', '6', '-', '(',
        '1', '2', '3', '*', ')',
        '0', '.', '=', '/', '%'
    ]

    def calculator(self, symbol: Button) -> None:
        """
        Обработка вычислений
        :param symbol:
        :return:
        """
        if symbol.text is 'AC':
            self.clear()  # Очищаем строку ввода
        elif symbol.text is 'pi':
            self.set_result(self.get_result() + '3.14')  # добавляем в строку число Пи
        elif symbol.text is 'mr':
            self.perform()
            self.memory = self.get_result()  # Сохраняем в память значение
        elif symbol.text is 'mc':
            self.memory = ''
        elif symbol.text is 'm':
            self.set_result(self.get_result() + self.memory)
        elif symbol.text is '<':
            self.remove_last_symbol()  # Удаляем последний символ
        elif symbol.text is not '=':
            value = self.get_result() + symbol.text
            self.set_result(value)
        else:
            self.perform()

    def perform(self) -> None:
        """
        Вычисление строки
        :return:
        """
        try:
            self.set_result(str(eval(self.result.text)))
        except (SyntaxError, NameError, ZeroDivisionError):
            self.set_result()

    def remove_last_symbol(self) -> None:
        """
        Удаление последнего символа
        :return:
        """
        self.set_result(self.get_result()[:-1])

    def clear(self) -> None:
        """
        Очистка строки ввода
        :return:
        """
        self.set_result()

    def set_result(self, value: str = '') -> None:
        """
        Передача значений в строку ввода
        :param value:
        :return:
        """
        self.result.text = value

    def get_result(self) -> str:
        """
        Получение занчений строки ввода
        :return:
        """
        return self.result.text

    def build(self) -> BoxLayout:
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
