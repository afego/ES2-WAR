import pygame
class JanelaPadrao:

    def __init__(self, janela):
        self.janela = janela
        


    def trataEvento(self):
        for e in pygame.event.get():
            self.evento(e)
    
    def evento(self, e):
        pass

    def draw(self):
        self.trataEvento()