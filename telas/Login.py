from telas.JanelaPadrao import JanelaPadrao
from PPlay.gameimage import GameImage
from  PPlay.mouse import Mouse
from componentes.campoTexto import CampoTexto
from componentes.campoSenha import CampoSenha
import pygame
from servico.Login import sign_in


"""botão provisorio preciso ser refeito com componente"""
class Login(JanelaPadrao):
    def __init__(self, janela):
        super().__init__(janela)
        self.bg = GameImage(image_file="./assets/imagem/tela_inicial/Credit-Marines-Flickr-CC-BY-NC-2.png")
        self.bg.set_scale(self.janela.width , self.janela.height)
        self.loginCampo = CampoTexto(janela,30, 30 ,40,10)
        self.senhaCampo = CampoSenha(janela,30, 50 ,40,10)
        self.botao = pygame.Rect([380,300,70,30])
        
        

    def draw(self):
        super().draw()
        self.bg.draw()
        self.loginCampo.draw()
        pygame.draw.rect(self.janela.get_screen(), (200,15,51),self.botao)
        self.senhaCampo.draw()

    def evento(self, e):
        super().evento(e)
        if e.type == pygame.MOUSEBUTTONDOWN and self.botao.collidepoint(Mouse().get_position()):
            token = sign_in(self.loginCampo.texto, self.senhaCampo.texto)
            if not token:
                print("Falha ao fazer o login")
            else:
                print("Login feito com sucesso")
        self.loginCampo.evento(e)
        self.senhaCampo.evento(e)
