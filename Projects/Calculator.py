# import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Set the App Size
Window.size = (400, 520)

Builder.load_file('./Calc.kv')


class MyLayout(Widget):

    def clear(self):
        self.ids.calc_input.text = '0'

    def number_button(self, button):

        prior = self.ids.calc_input.text

        if prior == '0':
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def add(self):

        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'

    def subtract(self):

        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'

    def multiply(self):

        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}x'

    def divide(self):

        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'

    def equals(self):

        prior = self.ids.calc_input.text

        if "+" in prior:
            num_list = prior.split("+")
            answer = 0

            for num in num_list:
                answer += int(num)

            self.ids.calc_input.text = str(answer)


class CalculatorApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
