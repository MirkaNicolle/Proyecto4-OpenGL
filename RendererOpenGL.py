'''
Source: https://pastebin.com/XDQyDZUd
        https://github.com/churly92/RendererOpenGL

Mirka Monzon 18139
Proyecto 4: OpenGL

'''

import pygame, sys
from pygame.locals import *
from pygame import mixer
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders
 
mainClock = pygame.time.Clock()

width = 960
height = 540

pygame.init()
pygame.display.set_caption('Proyecto 4: OpenGL')
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.OPENGL )
screen.set_alpha(None)
 
font = pygame.font.Font('freesansbold.ttf', 30)

#musica
mixer.music.load('SuperMarioGalaxy.wav')
mixer.music.play(-1)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:

        #fondo
        fondo = pygame.image.load('fondo.jpg')
        screen.blit(fondo, (0,0))

        draw_text('Space display menu', font, (255, 255, 255), screen, 300, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        draw_text('Tierra', font, (50, 100, 200, 50), screen, 400, 110)
        button_1 = pygame.Rect(350, 100, 200, 50)
        
        draw_text('Marte', font, (50, 200, 200, 50), screen, 400, 210)
        button_2 = pygame.Rect(350, 200, 200, 50)
        
        draw_text('Jupiter', font, (50, 100, 200, 50), screen, 400, 310)
        button_3 = pygame.Rect(350, 300, 200, 50)
        
        draw_text('Mercurio', font, (50, 200, 200, 50), screen, 390, 410)
        button_4 = pygame.Rect(350, 400, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            resaltado = pygame.Rect(350, 100, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), resaltado)
            if click:
                tierra()
        if button_2.collidepoint((mx, my)):
            resaltado = pygame.Rect(350, 200, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), resaltado)
            if click:
                marte()
        if button_3.collidepoint((mx,my)):
            resaltado = pygame.Rect(350, 300, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), resaltado)
            if click:
                jupiter()
        if button_4.collidepoint((mx,my)):
            resaltado = pygame.Rect(350, 400, 200, 50)
            pygame.draw.rect(screen, (255, 255, 255), resaltado)
            if click:
                mercurio()
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def tierra():
    running = True
    while running:
         
        #fondo
        fondo = pygame.image.load('fondo.jpg')
        screen.blit(fondo, (0,0))
        
        draw_text('tierra', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def marte():
    running = True
    while running:
        
        #fondo
        fondo = pygame.image.load('fondo.jpg')
        screen.blit(fondo, (0,0))
 
        draw_text('marte', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def jupiter():
    running = True
    while running:
        
        #fondo
        fondo = pygame.image.load('fondo.jpg')
        screen.blit(fondo, (0,0))
 
        draw_text('jupiter', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def mercurio():
    running = True
    while running:
        
        #fondo
        fondo = pygame.image.load('fondo.jpg')
        screen.blit(fondo, (0,0))
 
        draw_text('mercurio', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()