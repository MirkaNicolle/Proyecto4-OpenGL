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

width = 960
height = 540

pygame.init()
pygame.display.set_caption('Proyecto 4: OpenGL')
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE )
screen.set_alpha(None)

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 30)

#musica
mixer.music.load('SuperMarioGalaxy.wav')
mixer.music.play(-1)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
#click = False
 
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
        clock.tick(60)





#OBJ TIERRA
def tierra():
    running = True
    while running:
        
        screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.OPENGL)
        deltaTime = 0.0

        rend = Renderer(screen)
        rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

        model = Model('cube.obj', 'earth.jpg')
        model.position.z = -5

        rend.scene.append( model )

        keys = pygame.key.get_pressed()

        # Traslacion de camara
        if keys[K_d]:
            rend.camPosition.x += 1 * deltaTime
        if keys[K_a]:
            rend.camPosition.x -= 1 * deltaTime
        if keys[K_w]:
            rend.camPosition.z += 1 * deltaTime
        if keys[K_s]:
            rend.camPosition.z -= 1 * deltaTime
        if keys[K_q]:
            rend.camPosition.y -= 1 * deltaTime
        if keys[K_e]:
            rend.camPosition.y += 1 * deltaTime

        if keys[K_LEFT]:
            if rend.valor > 0:
                rend.valor -= 0.1 * deltaTime

        if keys[K_RIGHT]:
            if rend.valor < 0.2:
                rend.valor += 0.1 * deltaTime

        # Rotacion de camara
        if keys[K_z]:
            rend.camRotation.y += 15 * deltaTime
        if keys[K_x]:
            rend.camRotation.y -= 15 * deltaTime
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        rend.tiempo += deltaTime
        deltaTime = clock.tick(60) / 1000

        rend.render()

        pygame.display.flip()





#OBJ MARTE
def marte():
    running = True
    while running:
        
        screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.OPENGL)
        deltaTime = 0.0

        rend = Renderer(screen)
        rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

        model = Model('circle.obj', 'mars.jpg')
        model.position.z = -5

        rend.scene.append( model )

        keys = pygame.key.get_pressed()

        # Traslacion de camara
        if keys[K_d]:
            rend.camPosition.x += 1 * deltaTime
        if keys[K_a]:
            rend.camPosition.x -= 1 * deltaTime
        if keys[K_w]:
            rend.camPosition.z += 1 * deltaTime
        if keys[K_s]:
            rend.camPosition.z -= 1 * deltaTime
        if keys[K_q]:
            rend.camPosition.y -= 1 * deltaTime
        if keys[K_e]:
            rend.camPosition.y += 1 * deltaTime

        if keys[K_LEFT]:
            if rend.valor > 0:
                rend.valor -= 0.1 * deltaTime

        if keys[K_RIGHT]:
            if rend.valor < 0.2:
                rend.valor += 0.1 * deltaTime

        # Rotacion de camara
        if keys[K_z]:
            rend.camRotation.y += 15 * deltaTime
        if keys[K_x]:
            rend.camRotation.y -= 15 * deltaTime
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        rend.tiempo += deltaTime
        deltaTime = clock.tick(60) / 1000

        rend.render()

        pygame.display.flip()





#OBJ JUPITER
def jupiter():
    running = True
    while running:
        
        screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.OPENGL)
        deltaTime = 0.0

        rend = Renderer(screen)
        rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

        model = Model('cone.obj', 'jupiter.jpg')
        model.position.z = -5

        rend.scene.append( model )

        keys = pygame.key.get_pressed()

        # Traslacion de camara
        if keys[K_d]:
            rend.camPosition.x += 1 * deltaTime
        if keys[K_a]:
            rend.camPosition.x -= 1 * deltaTime
        if keys[K_w]:
            rend.camPosition.z += 1 * deltaTime
        if keys[K_s]:
            rend.camPosition.z -= 1 * deltaTime
        if keys[K_q]:
            rend.camPosition.y -= 1 * deltaTime
        if keys[K_e]:
            rend.camPosition.y += 1 * deltaTime

        if keys[K_LEFT]:
            if rend.valor > 0:
                rend.valor -= 0.1 * deltaTime

        if keys[K_RIGHT]:
            if rend.valor < 0.2:
                rend.valor += 0.1 * deltaTime

        # Rotacion de camara
        if keys[K_z]:
            rend.camRotation.y += 15 * deltaTime
        if keys[K_x]:
            rend.camRotation.y -= 15 * deltaTime
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        rend.tiempo += deltaTime
        deltaTime = clock.tick(60) / 1000

        rend.render()

        pygame.display.flip()




#OBJ MERCURIO
def mercurio():
    running = True
    while running:
        
        screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.OPENGL)
        deltaTime = 0.0

        rend = Renderer(screen)
        rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

        model = Model('cylinder.obj', 'mercury.jpg')
        model.position.z = -5

        rend.scene.append( model )

        keys = pygame.key.get_pressed()

        # Traslacion de camara
        if keys[K_d]:
            rend.camPosition.x += 1 * deltaTime
        if keys[K_a]:
            rend.camPosition.x -= 1 * deltaTime
        if keys[K_w]:
            rend.camPosition.z += 1 * deltaTime
        if keys[K_s]:
            rend.camPosition.z -= 1 * deltaTime
        if keys[K_q]:
            rend.camPosition.y -= 1 * deltaTime
        if keys[K_e]:
            rend.camPosition.y += 1 * deltaTime

        if keys[K_LEFT]:
            if rend.valor > 0:
                rend.valor -= 0.1 * deltaTime

        if keys[K_RIGHT]:
            if rend.valor < 0.2:
                rend.valor += 0.1 * deltaTime

        # Rotacion de camara
        if keys[K_z]:
            rend.camRotation.y += 15 * deltaTime
        if keys[K_x]:
            rend.camRotation.y -= 15 * deltaTime
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        rend.tiempo += deltaTime
        deltaTime = clock.tick(60) / 1000

        rend.render()

        pygame.display.flip()

main_menu()