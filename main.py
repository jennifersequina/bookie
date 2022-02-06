KIVY_NO_ARGS=1
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from downloader import downloader
from converter import converter
from sendtokindle import sendkindle


class Bookie(App):
    def __init__(self):
        super().__init__()
        self.downloaded_file_name = None
        self.converted_file_name = None

    def build(self):
        self._app_window = GridLayout()
        self._app_window.cols = 1
        self._app_window.size_hint = (0.6, 0.7)
        self._app_window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self._app_window.add_widget(Image(source="books.png"))
        self.main_text = Label(
                        text="Enter the title and author of the book you want to read",
                        font_size=34,
                        italic=True,
                        color="#FFB6C1")
        self._app_window.add_widget(self.main_text)
        self.user = TextInput(
                    multiline=False,
                    padding_y=(20, 20),
                    size_hint=(0.4, 0.3),
                    halign="center")
        self._app_window.add_widget(self.user)

        self.button1 = Button(
                    text="Search and Download",
                    size_hint=(0.4, 0.3),
                    bold=True,
                    background_color="#DB7093",
                    background_normal="")
        self.button1.bind(on_press=self.download)
        self._app_window.add_widget(self.button1)

        self.button2 = Button(
            text="Convert to MOBI",
            size_hint=(0.4, 0.3),
            bold=True,
            background_color="#FFB6C1",
            background_normal="")
        self.button2.bind(on_press=self.convert)
        self._app_window.add_widget(self.button2)

        self.button3 = Button(
            text="Send to Kindle",
            size_hint=(0.4, 0.3),
            bold=True,
            background_color="#FFC0CB",
            background_normal="")
        self.button3.bind(on_press=self.send)
        self._app_window.add_widget(self.button3)

        return self._app_window

    def download(self, instance):
        self.downloaded_file_name = downloader(self.user.text)
        self.main_text.text = "EPUB is now ready for processing"

    def convert(self, instance):
        self.converted_file_name = converter()
        self.main_text.text = "File has been converted to MOBI"

    def send(self, instance):
        sendkindle(self.converted_file_name)
        self.main_text.text = "MOBI file has been sent to Kindle"

if __name__ == "__main__":
    Bookie().run()