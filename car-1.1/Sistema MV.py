from pygame.locals import *
import pygame
from sys import exit
from random import randint

pygame.init()

madeiras = 1

largura = 640
altura = 480

x = largura / 2
y = 425

x2 = 400
y2 = 150

bateu = 0

fonte = pygame.font.SysFont('arial', 40, True, True)
fonte2 = pygame.font.SysFont('arial', 40, True, True)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CARS')
relg = pygame.time.Clock()

while True:
    relg.tick(30)
    mensagem = f'Bateu: {bateu}'
    mensagem2 = f'Morreu Você bateu {bateu} vezes'
    texto_f2 = fonte.render(mensagem, True, (100, 0, 0))

    texto_f = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_UP:
                y = y - 30
            if event.key == K_DOWN:
                y = y + 30
            if event.key == K_RIGHT:
                x = x + 30
            if event.key == K_LEFT:
                x = x - 30'''

        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20

        if pygame.key.get_pressed()[K_HOME]:
            x = largura / 2
            y = 425

        if pygame.key.get_pressed()[K_F8]:
            x = 550
            y = 425

        if pygame.key.get_pressed()[K_F11]:
            x = 80
            y = 425

        if pygame.key.get_pressed()[K_f]:
            madeiras = madeiras + 5
            print(f'{madeiras}')

        # if event.type == KEYDOWN:
        #     if pygame.key.get_pressed() [K_l]:
        #         madeiras = (madeiras * 10) + madeiras * 10 * madeiraslllllll
        #         print(f'{madeiras}')




        pygame.display.update()

    j = 0
    d = 0
    k = 490
    g= 480
    pygame.draw.rect(tela, (0, 110, 0), (j, d, 160, 480))
    pygame.draw.rect(tela, (0, 110, 0), (k, d, 160, 480))
    pygame.draw.rect(tela, (70, 70, 70), (150, d, 360, 480))
    '''pygame.draw.circle(tela, (255, 0, 201), (650, 250), (1000))'''
    pista_1= pygame.draw.line(tela, (255, 255, 0), (150, 0), (150, altura), (30))
    pista_2 = pygame.draw.line(tela, (255, 255, 0), (500, 0), (500, altura), (30))
    car = pygame.draw.rect(tela, (255, 0, 255), (x, y, 40, 50))



    y2 = y2 +2


    car_2 = pygame.draw.rect(tela, (100, 90, 50), (x2, y2, 40, 50))
    esrs = (pygame.draw.rect(tela, (100, 190, 250), (x2 - 200, y2 + 190, 40, 50)))
    uyfi = (pygame.draw.rect(tela, (250, 230, 250), (x2 - 200, y2, 40, 50)))
    uyfi2 = (pygame.draw.rect(tela, (255, 200, 0), (136, 30, 30, 40)))
    if y2 >= altura:
        y2 = 0
        esrs = (pygame.draw.rect(tela, (100, 190, 250), (x2 - 100, y2 + 150, 40, 50)))

    if car.colliderect(pista_1):
        x = 1000000
        y = 1000000
        bateu = bateu + 1

    if car.colliderect(pista_2):
        x = 1000000
        y = 1000000
        bateu = bateu + 1

    if car.colliderect(esrs):
        x = 1000000
        y = 1000000
        bateu = bateu + 11


    if car.colliderect(uyfi):
        x = 1000000
        y = 1000000
        bateu = bateu + 1


    if car.colliderect(uyfi2):
        x = 1000000
        y = 1000000
        bateu = 0

    if car.colliderect(car_2):
        x = 1000000
        y = 1000000
        bateu = bateu + 4


    if bateu >= 12:
        print('nada')
        pygame.quit()
        exit()

        bateu = bateu + 0

    if y == (12):
        y = 425

    tela.blit(texto_f2, (251, 30))
    tela.blit(texto_f, (250, 30))

    pygame.display.update()




class Pessosoa:
    def __int__(self, CPF, nascimento, cildade):
        self.ciucade = cildade
        self.naciment = nascimento
        self.CPF = CPF




