from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#from pyfirmata import Arduino, util
#import time

class PaginaInicial(ScreenManager):
    pass


class Menu(Screen):
    pass

class Controles(Screen):
    status = False
    #placa = Arduino("COM3")

    #placa.digital[7].write(1)

    def statusLampada(self):

        self.status = not self.status
        self.ids.btlamp.text = 'Desligar Lampada' if self.status else 'Ligar Lampada'

        '''if self.ids.btlamp.text == 'Desligar Lampada':
            self.placa.digital[7].write(0)
        else:
            self.placa.digital[7].write(1)'''

    def statusVentilador(self):
        self.status = not self.status
        self.ids.btvent.text = 'Desligar Ventilador' if self.status else 'Ligar Ventilador'

       #if self.ids.btvent.text == 'Desligar Ventilador':
            #self.placa.digital[5].write(1)
        #else:
            #self.placa.digital[5].write(0)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        App.get_running_app().root.current = 'menu'
        return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def mudarTexto(self, buttonl):
        self.buttonl.text = 'Desligar lampada'

    

class Automatizacao(App):
    def build(self):
        return PaginaInicial()

Automatizacao().run()