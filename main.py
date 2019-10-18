import pygame
import time

pygame.init()

largeur = 500
hauteur = 300
fenetre = pygame.display.set_mode((largeur,hauteur))

i=1;
continuer=1
while continuer:
    horloge.tick(FPS)

    i += 1
    print(i)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
pygame.quit()
