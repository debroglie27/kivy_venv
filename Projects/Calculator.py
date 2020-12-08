# import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Set the App Size
Window.size = (400, 520)

Builder.load_file('./Calc.kv')


class MyLayout(Widget):
    math_symbol_clicked = 0

    def clear(self):
        self.ids.calc_input.text = '0'

    def number_button(self, button):

        prior = self.ids.calc_input.text

        if "Error!" in prior:
            prior = ''

        if prior == '0':
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # For '<<' Button
    def remove(self):

        prior = self.ids.calc_input.text
        if len(prior) == 1:
            self.ids.calc_input.text = '0'
        else:
            self.ids.calc_input.text = prior[:-1]

    # For '+/-' Button
    def pos_neg(self):

        prior = self.ids.calc_input.text
        if prior == '0':
            return
        if prior[0] == '-':
            self.ids.calc_input.text = f'{prior[1:]}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # For '.' Button
    def dot(self):

        prior = self.ids.calc_input.text
        if '.' in prior and self.math_symbol_clicked == 0:
            return
        self.ids.calc_input.text = f'{prior}.'
        self.math_symbol_clicked = 0

    # For '+', '-', 'x', '/' Symbols
    def math_sign(self, sign):

        self.math_symbol_clicked = 1
        prior = self.ids.calc_input.text

        if "Error!" in prior:
            self.ids.calc_input.text = '0'
            return

        self.ids.calc_input.text = f'{prior}{sign}'

    # For '=' Button
    def equals(self):

        prior = self.ids.calc_input.text
        try:
            # Evaluate the output
            answer = eval(prior)
        except Exception:
            answer = "Error!"

        self.ids.calc_input.text = str(answer)


class CalculatorApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
