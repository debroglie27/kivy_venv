# import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('../Design_Files/img_view.kv')


# Main Grid
class MyLayout(Widget):

    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except Exception:
            pass


class AwesomeApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
