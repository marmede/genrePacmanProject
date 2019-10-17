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

def supprimerElts(tab):
    newTab = []
    for e in tab:
        if e.isAlive():
            newTab.append(e)
    return newTab

def lireImages():
    images = {}
    images["balle"]=[]
    images["balle"].append(pygame.image.load("ressources/apple.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-02.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-03.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-04.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-05.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-06.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-07.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-08.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-09.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-10.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-11.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-12.png").convert_alpha())
    images["balle"].append(pygame.image.load("ressources/apple-13.png").convert_alpha())

    images["boost"] = []
    images["boost"].append(pygame.image.load("ressources/boost (1).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (2).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (3).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (4).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (5).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (6).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (7).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (8).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (9).png").convert_alpha())
    images["boost"].append(pygame.image.load("ressources/boost (10).png").convert_alpha())

    images["health"] = []
    images["health"].append(pygame.image.load("ressources/frame-1.png").convert_alpha())
    images["health"].append(pygame.image.load("ressources/frame-2.png").convert_alpha())
    images["health"].append(pygame.image.load("ressources/frame-3.png").convert_alpha())
    images["health"].append(pygame.image.load("ressources/frame-4.png").convert_alpha())
    images["health"].append(pygame.image.load("ressources/frame-5.png").convert_alpha())
    images["health"].append(pygame.image.load("ressources/frame-6.png").convert_alpha())
    images["health"].append(pygame.image.load("ressources/frame-7.png").convert_alpha())
    images["health"].append(pygame.image.load("ressources/frame-8.png").convert_alpha())

    images["perso"] = []
    images["perso"].append(pygame.image.load("ressources/player/down_1.png").convert_alpha())    
    
    images["perso_down"] = []
    images["perso_down"].append(pygame.image.load("ressources/player/down_1.png").convert_alpha())
    images["perso_down"].append(pygame.image.load("ressources/player/down_2.png").convert_alpha())
    images["perso_down"].append(pygame.image.load("ressources/player/down_3.png").convert_alpha())
    images["perso_down"].append(pygame.image.load("ressources/player/down_4.png").convert_alpha())

    images["perso_shield_down"] = []
    images["perso_shield_down"].append(pygame.image.load("ressources/player/down_1.png").convert_alpha())
    images["perso_shield_down"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_down"].append(pygame.image.load("ressources/player/down_2.png").convert_alpha())
    images["perso_shield_down"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_down"].append(pygame.image.load("ressources/player/down_3.png").convert_alpha())
    images["perso_shield_down"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_down"].append(pygame.image.load("ressources/player/down_4.png").convert_alpha())

    images["perso_left"] = []
    images["perso_left"].append(pygame.image.load("ressources/player/left_1.png").convert_alpha())
    images["perso_left"].append(pygame.image.load("ressources/player/left_2.png").convert_alpha())
    images["perso_left"].append(pygame.image.load("ressources/player/left_3.png").convert_alpha())
    images["perso_left"].append(pygame.image.load("ressources/player/left_4.png").convert_alpha())

    images["perso_shield_left"] = []
    images["perso_shield_left"].append(pygame.image.load("ressources/player/left_1.png").convert_alpha())
    images["perso_shield_left"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_left"].append(pygame.image.load("ressources/player/left_2.png").convert_alpha())
    images["perso_shield_left"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_left"].append(pygame.image.load("ressources/player/left_3.png").convert_alpha())
    images["perso_shield_left"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_left"].append(pygame.image.load("ressources/player/left_4.png").convert_alpha())
    
    images["perso_right"] = []
    images["perso_right"].append(pygame.image.load("ressources/player/right_1.png").convert_alpha())
    images["perso_right"].append(pygame.image.load("ressources/player/right_2.png").convert_alpha())
    images["perso_right"].append(pygame.image.load("ressources/player/right_3.png").convert_alpha())
    images["perso_right"].append(pygame.image.load("ressources/player/right_4.png").convert_alpha())

    images["perso_shield_right"] = []
    images["perso_shield_right"].append(pygame.image.load("ressources/player/right_1.png").convert_alpha())
    images["perso_shield_right"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_right"].append(pygame.image.load("ressources/player/right_2.png").convert_alpha())
    images["perso_shield_right"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_right"].append(pygame.image.load("ressources/player/right_3.png").convert_alpha())
    images["perso_shield_right"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_right"].append(pygame.image.load("ressources/player/right_4.png").convert_alpha())

    images["perso_up"] = []
    images["perso_up"].append(pygame.image.load("ressources/player/up_1.png").convert_alpha())
    images["perso_up"].append(pygame.image.load("ressources/player/up_2.png").convert_alpha())
    images["perso_up"].append(pygame.image.load("ressources/player/up_3.png").convert_alpha())
    images["perso_up"].append(pygame.image.load("ressources/player/up_4.png").convert_alpha())

    images["perso_shield_up"] = []
    images["perso_shield_up"].append(pygame.image.load("ressources/player/up_1.png").convert_alpha())
    images["perso_shield_up"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_up"].append(pygame.image.load("ressources/player/up_2.png").convert_alpha())
    images["perso_shield_up"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_up"].append(pygame.image.load("ressources/player/up_3.png").convert_alpha())
    images["perso_shield_up"].append(pygame.image.load("ressources/player/down_5.png").convert_alpha())
    images["perso_shield_up"].append(pygame.image.load("ressources/player/up_4.png").convert_alpha())

    images["shield"] = []
    images["shield"].append(pygame.image.load("ressources/AngelShieldEffect_Icon (1).png").convert_alpha())
    images["shield"].append(pygame.image.load("ressources/AngelShieldEffect_Icon (2).png").convert_alpha())
    images["shield"].append(pygame.image.load("ressources/AngelShieldEffect_Icon (3).png").convert_alpha())
    images["shield"].append(pygame.image.load("ressources/AngelShieldEffect_Icon (4).png").convert_alpha())
    images["shield"].append(pygame.image.load("ressources/AngelShieldEffect_Icon (5).png").convert_alpha())

    return images

def chargerPlaylist(n):
    pygame.mixer.music.load(n)

def chargerBruitages():
    musiques = {}
    musiques["vitesse"] = pygame.mixer.Sound("ressources/SoundPack01/Coin01.ogg")
    musiques["vie"] = pygame.mixer.Sound("ressources/SoundPack01/Rise02.ogg")
    musiques["touche"] = pygame.mixer.Sound("ressources/SoundPack01/classic_hurt.ogg")

    return musiques

def lireMusique():
    pygame.mixer.music.play()

def stopMusique():
    pygame.mixer.music.stop()

def creerBalle(i, tab, image):
    if i%100 == 0:
        tab.append(BalleAnimee(image, 230, 300))
    return tab

def creerBonus(i, FPS, tab, image1, image2, image3):
    if i%(5*FPS) == 0:
        if random.randint(0, 1) < 0.3:
            tab.append(BonusAnimee(images["boost"], random.randint(0,550), 0))
        elif random.randint(0, 1) < 0.6:
            tab.append(BonusAnimee(images["health"], random.randint(0,550), 0))
        else:
            tab.append(BonusAnimee(images["shield"], random.randint(0,550), 0))

    return tab

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

perso = PersoAnimee(images["perso"], images["perso_up"], images["perso_down"], images["perso_left"], images["perso_right"], images["perso_shield_up"], images["perso_shield_down"], images["perso_shield_left"], images["perso_shield_right"],random.randint(0, 500), random.randint(0,350))

balle = BalleAnimee(images["balle"], random.randint(0, 500), random.randint(0,350))

balles_list = []
balles_list.append(balle)

bonus_list = []

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
        perso.afficher(fenetre)
        viesText.afficher(fenetre)

        balles_list = creerBalle(i, balles_list, images["balle"])

        bonus_list = creerBonus(i, FPS, bonus_list, images["boost"], images["health"], images["shield"])

        for bonus in bonus_list:
            bonus.afficher(fenetre)
            bonus.deplacer()

            if bonus.rect.y >= hauteur:
                bonus.vie = False

            bonus.collide(perso, images, musiques)

        bonus_list = supprimerElts(bonus_list)

        perso.effetBoost(FPS)
            
        for balles in balles_list:
            balles.afficher(fenetre)
            balles.deplacement()

            balles.rebond(fenetre)

            balles.collisionEnnemi(perso, musiques)
            if perso.isAlive() == False:
                changerPlaylist = 1
                stopMusique()
                gameover = 1
                fin = 1
        balles_list = supprimerElts(balles_list)
        
    if gameover and fin:
        balles_list = []
        bonus_list = []
        
        if changerPlaylist:
            chargerPlaylist("ressources/TownTheme.mp3")
            lireMusique()
            changerPlaylist = 0
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
