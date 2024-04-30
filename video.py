# Widgets Básicos: Video

from kivy.app import App
from kivy.uix.video import Video



class MinhaApp(App):
    def build(self):
        video = Video(source='/Users/aluno.sesipaulista/Documents/Teste_App/video/teste.mp4', size_hint = (1,1), options = {'fit_mode': 'contain'})
        video.state='play'
        video.options = {'eos': 'loop'}
        video.allow_stretch=True
        return video

if __name__ == "__main__":
    MinhaApp().run()