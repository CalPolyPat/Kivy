from kivy.app import App
from kivy.uix.widget import Widget


class Overlay(Widget):
    pass


class CameraApp(App):
    def build(self):
        return Overlay()


if __name__ == '__main__':
    CameraApp().run()
