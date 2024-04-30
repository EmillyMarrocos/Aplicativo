# Widgets Básicos: Image(no próprio PC)

from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source=r'C:/Users/emill/Documents/Teste_App/img/OIP.jpg')

if __name__ == "__main__":
    MinhaApp().run()