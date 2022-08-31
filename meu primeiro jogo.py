import pygame
from pygame.locals import *
from sys import exit
from random import randint

'''ÁREA DE VARIAVEIS '''

largura = 640
altura = 480
x = int(largura / 2)
y = int(altura / 2)
x_circle1 = randint(40, 600)
y_circle1 = randint(50, 430)
velocidade = 15

pygame.init()

fonte = pygame.font.SysFont('arial',40,True,True)
pontos = 0
raio = 2
pygame.mixer.music.set_volume(0.07)
musica_de_fundo = pygame.mixer.music.load('BoxCatGamesCPUTalk.mp3')
som_coin = pygame.mixer.Sound('smw_coin.wav')


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olá mundo')

clock = pygame.time.Clock()
pygame.mixer.music.play(-1)
while True:
    clock.tick(60)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos:{pontos}'

    texto_formatado = fonte.render(mensagem, True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        ''' Tentativa de mover um circulo 
            if event.type == KEYDOWN:
            if event.key == K_a:
               x -= 20
            elif event.key == K_d:
                x += 20
            elif event.key == K_w:
                y -= 20
            elif event.key == K_s:
                y += 20
        '''
    '''Parte do movimentos do circulo'''
    if pygame.key.get_pressed()[K_a]:
        x -= velocidade
    elif pygame.key.get_pressed()[K_d]:
        x += velocidade
    elif pygame.key.get_pressed()[K_w]:
        y -= velocidade
    elif pygame.key.get_pressed()[K_s]:
        y += velocidade

    circle1 = pygame.draw.circle(tela, (255, 0, 0), (x, y), raio)
    circle = pygame.draw.circle(tela, (0, 255, 0), (x_circle1, y_circle1), 30)

    if circle.colliderect(circle1):
        x_circle1 = randint(40, 600)
        y_circle1 = randint(50, 430)
        pontos = pontos + 1
        som_coin.play()
        if raio <= 200:
            raio += 5

    tela.blit(texto_formatado,(50,40))
    pygame.display.update()
