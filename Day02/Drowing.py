#Pygame 드로잉 에디터
import pygame, sys
from pygame.locals import *
width, height = 500, 500
radius = 10
mouseX, mouseY = 0, 0
pygame.init()
window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(255,255,255))
fps = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                window.fill(pygame.Color(255,255,255))
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        mouseX, mouseY = pygame.mouse.get_pos()
        b = pygame.mouse.get_pressed()
        if b[0] == 1:
            pygame.draw.circle(window, pygame.Color(255,0,0),
                               (mouseX, mouseY), radius, radius)
    pygame.display.update()
    fps.tick(30)