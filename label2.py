#Label - "halign" e "valign"

from kivy.app import App 
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(
            text= "Olá SENAI!", 
            halign= "left", #Alinha o texto á esquerda
            valign= "top", #Alinha o texto ao topo
            size_hint= (None, None), #Desativa o ajusto automático do tamanho
            size= (150, 50), #Define o tamanho do rótulon
            text_size= (150, None) #Define a largura máxima do texto
        )
    
if __name__ == "__main__":
    MinhaApp().run()