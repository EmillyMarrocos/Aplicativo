# Widgets Básicos: Video

from kivy.app import App
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        video = Video(source='C:/Users/emill/Documents/Teste_App/video/Sylvia Salustti, Raphael Rossato - Vejo Enfim a Luz Brilhar (De.mp4')
        return video

if __name__ == "__main__":
    MinhaApp().run()