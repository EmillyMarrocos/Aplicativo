'''# Widgets Básicos: BoxLayout
# BoxLayout: Orientação
# BoxLayout: Adicionando Widgets
# BoxLayout: Espaçamento e Alinhamento
# BoxLayout: Exemplo Prático

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation= 'horizontal', spacing=10, padding=[20, 10])
        botao1 = Button(text= 'Botão 1')
        botao2 = Button(text= 'Botão 2')
        botao3 = Button(text= 'Botão 3')

        layout.add_widget(botao1)
        layout.add_widget(botao2)
        layout.add_widget(botao3)
        return layout

MinhaApp().run()'''

'''# Widgets Básicos: BoxLayout
# BoxLayout: Orientação
# BoxLayout: Adicionando Widgets
# BoxLayout: Espaçamento e Alinhamento
# BoxLayout: Exemplo Prático (Vertical)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation= 'vertical', spacing=10, padding=[20, 10])
        botao1 = Button(text= 'Botão 1')
        botao2 = Button(text= 'Botão 2')
        botao3 = Button(text= 'Botão 3')

        layout.add_widget(botao1)
        layout.add_widget(botao2)
        layout.add_widget(botao3)
        return layout

MinhaApp().run()'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation= 'vertical', spacing=10)

        # Criando e adicionando um botão com texto, cor de fundo e tamanho de fonte personalizados
        btn1 = Button(text='Botão 1', background_color=(0.2, 0.7, 0.3, 1), font_size=20)
        layout.add_widget(btn1)

        # Criando e adicionando um botão com um texto diferente e alinhamento horizontal personalizado
        btn2 = Button(text='Clique aqui!', halign= 'center')
        layout.add_widget(btn2)

        # Criando e adicionando um botão com um texto grando e cor de fundo personalizada
        btn3 = Button(text='Clique para continuar', background_color= (0.9, 0.5, 0.1, 1), font_size= 30)
        layout.add_widget(btn3)
        
        # Criando e adicionando um botão com uma ação personalizada ao ser pressionado
        def acao_botao(instance):
            instance.text = 'Botão Pressionado!'
        btn4 = Button(text='Botão 4')
        btn4.bind(on_press=acao_botao)
        layout.add_widget(btn4)

        # Adicionando um rótulo para exibir informações adicionais
        info_label = Label(text= 'Pressione os botões para ver diferentes propriedades em ação.')
        layout.add_widget(info_label)

        return layout
    
if __name__ == "__main__":
    MinhaApp().run()