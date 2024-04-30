# Widgets Básicos: Carousel/Personalizando

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage

class CarouselApp(App):
    def build(self):
        # Criando um Carousel
        carousel= Carousel(direction= 'right', loop= True)

        # Adicionando widgets ao Carousel
        for i in range(3):
            label= Label(text= 'Slide: {}'.format(i+1))
            carousel.add_widget(label)

        # Adicionando imagens ao Carousel
        imagens = ['senaipe.jpg', 'sesi.jpg', 'iel.jpeg']
        for imagem in imagens:
            imagem_widget= AsyncImage(source= imagem)
            carousel.add_widget(imagem_widget)

            return carousel
        
if __name__ == "__main__":
   CarouselApp().run()