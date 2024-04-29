from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source='https://www.bing.com/images/blob?bcid=soKNIZc6AfcGEg')

if __name__ == "__main__":
    MinhaApp().run