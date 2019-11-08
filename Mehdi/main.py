import pygame
import random
from pygame.locals import *
from random import randint
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from JoueurAnimee import JoueurAnimee
from BalleAnimee import BalleAnimee
from BonusAnimee import BonusAnimee
from BalleTiree import BalleTiree
from Niveau import Niveau
from Fantome import Fantome

def resizeImg(tab):
        newTab =[]
        for img in tab:
                img = pygame.transform.scale(img, (70,70))
                newTab.append(img)

        return newTab

def lireImages():
        
        images = {}
        images["barre"] = [pygame.image.load("images/barre.png").convert_alpha()]
        images["barre2"] = [pygame.image.load("images/barreCopie.png").convert_alpha()]
        images["balle"] = [pygame.image.load("images/balle.png").convert_alpha()]
        images["background"] = [pygame.image.load("images/background2.jpg").convert()]
        images["chomp"] = [pygame.image.load("images/Balle/chomp1.png").convert_alpha()]
        images["luffy"] = {}
        images["luffy"]["debout"] = [pygame.image.load("images/Luffy/row-1-col-1.png").convert_alpha()]
        images["luffy"]["hit"] = [pygame.image.load("images/Luffy/hit.png").convert_alpha()]

        images["luffy"]["face"] = []
        images["luffy"]["face"].append(pygame.image.load("images/Luffy/row-1-col-1.png").convert_alpha())
        images["luffy"]["face"].append(pygame.image.load("images/Luffy/row-1-col-2.png").convert_alpha())
        images["luffy"]["face"].append(pygame.image.load("images/Luffy/row-1-col-3.png").convert_alpha())
        images["luffy"]["face"].append(pygame.image.load("images/Luffy/row-1-col-4.png").convert_alpha())
        images["luffy"]["face"].append(pygame.image.load("images/Luffy/row-1-col-5.png").convert_alpha())

        images["luffy"]["gauche"] = []
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-1.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-2.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-3.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-4.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-5.png").convert_alpha())

        images["luffy"]["droite"] = []
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-1.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-2.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-3.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-4.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-5.png").convert_alpha())

        images["luffy"]["dos"] = []
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-1.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-2.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-3.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-4.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-5.png").convert_alpha())

        images["mur"] = [pygame.image.load("images/lava_ground_cracked_tileset.png").convert_alpha()]

        images["blinky"] = {}
        images["blinky"]["debout"] = [pygame.image.load("images/blinky-b-1.png").convert_alpha()]
        
        images["blinky"]["haut"] = []
        images["blinky"]["haut"].append(pygame.image.load("images/blinky-t-1.png").convert_alpha())
        images["blinky"]["haut"].append(pygame.image.load("images/blinky-t-2.png").convert_alpha())

        images["blinky"]["bas"] = []
        images["blinky"]["bas"].append(pygame.image.load("images/blinky-b-1.png").convert_alpha())
        images["blinky"]["bas"].append(pygame.image.load("images/blinky-b-2.png").convert_alpha())

        images["blinky"]["gauche"] = []
        images["blinky"]["gauche"].append(pygame.image.load("images/blinky-l-1.png").convert_alpha())
        images["blinky"]["gauche"].append(pygame.image.load("images/blinky-l-2.png").convert_alpha())

        images["blinky"]["droit"] = []
        images["blinky"]["droit"].append(pygame.image.load("images/blinky-d-1.png").convert_alpha())
        images["blinky"]["droit"].append(pygame.image.load("images/blinky-d-2.png").convert_alpha())

        images["blinky"]["debout"] = resizeImg(images["blinky"]["debout"])
        images["blinky"]["haut"] = resizeImg(images["blinky"]["haut"])
        images["blinky"]["bas"] = resizeImg(images["blinky"]["bas"])
        images["blinky"]["gauche"] = resizeImg(images["blinky"]["gauche"])
        images["blinky"]["droit"] = resizeImg(images["blinky"]["droit"])
        return images

def creerballe(touches):
    if touches[K_SPACE]:
        balle.append(BalleAnimee(images["luffy"]["debout"]))

def creerEnnemies(tour,x):
    if (tour%20) == 0:
        ennemies.append(BalleAnimee(images["balle"],0,-50))

def supprimerElements(tab):
    newTab = []
    for e in tab:
        if e.isAlive():
            newTab.append(e)
    return newTab


pygame.init()
x_fen = 700
y_fen = 550
fenetre = pygame.display.set_mode((x_fen,y_fen))
#pygame.display.set_mode((0,0),pygame.FULLSCREEN)
images = lireImages();
#Les tableaux des éléments
balle = []
ennemies = []
tire=[]
lab = []


fond = ElementGraphiqueAnimee(images["background"],0,0)
perso = JoueurAnimee(images["luffy"],250,100)

fantome = Fantome(images["blinky"], 0, 0)

bloc = ElementGraphique(images["mur"],100,100)

game_over = False
continuer = True

#Tour == variable de temps
tour = 0


while continuer:
        tour += 1
        framerate = pygame.time.Clock()
        Fps = framerate.tick(30)
        #Affichage images
        fond.afficher((fenetre))
        #Atribution des touches
        touches = pygame.key.get_pressed()
        niveau = Niveau("niveau/niveauTest.txt", images["mur"])
        lab = niveau.createLab(y_fen,x_fen,bloc.rect.h,bloc.rect.w)
        niveau.afficherLab(lab,images["mur"],fenetre)

        #print(lab)

        perso.afficher(fenetre)
        fantome.afficher(fenetre)

        if touches [pygame.K_z]:
            perso.numimage += 1
            perso.direction = "gauche"

        a = (perso.rect.x)
        b = (perso.rect.y)
        haut  = ElementGraphiqueAnimee(images["barre"],a,b+2)
        haut.afficher((fenetre))

        bas = ElementGraphiqueAnimee(images["barre"],a,b+perso.rect.width)
        bas.afficher(fenetre)

        gauche = ElementGraphiqueAnimee(images["barre2"],a,b)
        gauche.afficher(fenetre)

        droite = ElementGraphiqueAnimee(images["barre2"],a+perso.rect.height-5,b)
        droite.afficher(fenetre)

        perso.Deplacer(touches,bloc)

        fantome.Deplacer(fenetre)
        
        #print(perso.rect.width)
        creerballe(touches)
        creerEnnemies(tour,x_fen)
        # if bloc.rect.collidepoint(perso.rect.x+(perso.rect.width/2),perso.rect.y) == True:
        #     print("haut")
        # if bloc.rect.collidepoint(perso.rect.x,perso.rect.y+(perso.rect.height/2)) == True:
        #     print("gauche")

        # if bloc.rect.collidepoint(perso.rect.x+(perso.rect.width/2),perso.rect.y+(perso.rect.height)) == True:
        #     print("bas")
        # if bloc.rect.collidepoint(perso.rect.x+(perso.rect.width),perso.rect.y+(perso.rect.height/2)) == True:
        #     print("droite")

        if bloc.rect.colliderect(perso.rect) == True:
            print("OUIIIIIIIII")

        #Afficher et deplacer les éléments d'un tableaux 
        for b in balle:
            b.afficher((fenetre))
            b.Deplacer(x_fen,y_fen)

        for e in ennemies:
            e.afficher((fenetre))
            e.Tombe(x_fen,y_fen)
            e.collide(perso)

        for t in tire:
            t.afficher((fenetre))
            t.Tire(x_fen,y_fen)


        bloc.afficher((fenetre))

        #print(perso.collision, perso.direction)

        #Mort du perso
        if perso.isAlive() == False:
            game_over = True
        ######################################

        ######################################

        #Suppressions des éléments inutiles (mort ou hors écran)
        balle = supprimerElements(balle)
        ennemies = supprimerElements(ennemies)
        tire = supprimerElements(tire)

        pygame.display.flip()

        for event in pygame.event.get():
            tire, images = perso.shoot(touches, event, tire, images)
            if event.type == pygame.QUIT or touches[K_ESCAPE]:
                continuer = False

pygame.quit()

        
