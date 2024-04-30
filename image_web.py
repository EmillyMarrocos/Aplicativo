# Widgets Básicos: Image(na Web)

from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        layout = BoxLayout()
        url = 'https://imagoi.com/wp-content/uploads/2021/01/Rapunzel-e-Jose-dancando-imagoi.jpg'
        image = AsyncImage(source=url)
        layout.add_widget(image)
        return layout

if __name__ == "__main__":
    MinhaApp().run()