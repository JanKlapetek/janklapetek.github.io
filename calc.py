from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/', '^', '√', 'sin', 'cos', 'tan']
        self.last_operator = None

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Výstupní pole
        self.result = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=32
        )
        self.layout.add_widget(self.result)

        # Tlačítka
        buttons = [
            ['C', '=',],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],
            ['sin', 'cos', 'tan', '√'],
            ['^', '(', ')', '.'],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    font_size=24,
                    on_press=self.on_button_press
                )
                h_layout.add_widget(button)
            self.layout.add_widget(h_layout)

        return self.layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.result.text = ""
        elif text == "=":
            try:
                expression = self.result.text
                expression = expression.replace('^', '**')
                expression = expression.replace('√', 'math.sqrt')
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                self.result.text = str(eval(expression))
            except Exception as e:
                self.result.text = "Error"
        else:
            self.result.text += text

if __name__ == '__main__':
    CalculatorApp().run()