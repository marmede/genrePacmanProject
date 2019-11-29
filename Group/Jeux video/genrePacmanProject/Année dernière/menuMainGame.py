import time
import pygame
from pygame.locals import *
import random
from Images import Images
from Perso import Perso
from Balle import Balle
from ImagesAnimee import ImagesAnimee
from BalleAnimee import BalleAnimee
from BonusAnimee import BonusAnimee
from PersoAnimee import PersoAnimee

def recommencer():
    perso.rect.x = random.randint(0, 500)
    perso.rect.y = random.randint(0, 350)
    perso.deltaX = 3
    perso.deltaY = 3

pygame.init()

largeur = 604
hauteur = 430
fenetre=pygame.display.set_mode((largeur,hauteur))

images = lireImages()

musiques = chargerBruitages()

image = pygame.image.load("ressources/bourse.jpg").convert()
fond = Images(image, 0, 0)

font = pygame.font.Font(None, 34)

image = font.render('<Escape> pour quitter', True, (0, 0, 0))
quitter = Images(image, 10, 10)

imageRestart = font.render('RECOMMENCER', True, (0, 0, 0))
reprendre = Images(imageRestart, largeur/3+40, hauteur/3+50)

image = font.render('GAME OVER', True, (0, 0, 0))
gameoverText = Images(image, largeur/3, hauteur/3)

image = font.render('Bienvenido amigo', True, (0, 0, 0))
menuText = Images(image, largeur/3, hauteur/3)

imageJouer = font.render('JOUER', True, (0, 0, 0))
jouerText = Images(imageJouer, largeur/3+40, hauteur/3+70)

horloge = pygame.time.Clock()

FPS = 60

gameover = 0

fin = 1
restart = 0
changerPlaylist = 0

i=1;
continuer=1
while continuer:

    image = font.render(str(perso.vies)+' vies restantes', True, (0, 0, 0))
    viesText = Images(image, 10, 400)

    horloge.tick(FPS)

    i += 1
    print(i)

    touches = pygame.key.get_pressed();
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if restart :
        balles_list.append(balle)
        recommencer()
        restart = 0

    if touches[pygame.K_ESCAPE] :
        continuer=0

    perso.deplacer(touches, fenetre)

    fond.afficher(fenetre)

    if gameover == 0 and fin:
        quitter.afficher(fenetre)
        menuText.afficher(fenetre)
        jouerText.afficher(fenetre)

        if jouerText.rect.collidepoint(mouse):
            imageJouer = font.render('JOUER', True, (255, 0, 0))
            jouerText = Images(imageJouer, largeur/3+40, hauteur/3+70)
            
            if click[0]:
                stopMusique()
                chargerPlaylist("ressources/01 game-game_0.ogg")
                lireMusique()
                fin = 0
        else:
            imageJouer = font.render('JOUER', True, (0, 0, 0))
            jouerText = Images(imageJouer, largeur/3+40, hauteur/3+70)
    
    if gameover == 0 and fin !=1:
        
        for balles in balles_list:
            if perso.isAlive() == False:
                gameover = 1
                fin = 1
        
    if gameover and fin:
        
        gameoverText.afficher(fenetre)
        reprendre.afficher(fenetre)
        
        if reprendre.rect.collidepoint(mouse):
            imageRestart = font.render('RECOMMENCER', True, (255, 0, 0))
            reprendre = Images(imageRestart, largeur/3-15, hauteur/3+50)
            
            if click[0]:
                gameover = 0
                perso.vies = 3
                restart = 1
        else:
            imageRestart = font.render('RECOMMENCER', True, (0, 0, 0))
            reprendre = Images(imageRestart, largeur/3-15, hauteur/3+50)


    
    quitter.afficher(fenetre)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

pygame.quit()
