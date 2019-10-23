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

def lireImages():
        
        images = {}
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

        images["mur"] = pygame.image.load("images/lava_ground_cracked_tileset.png").convert_alpha()
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

fond = ElementGraphiqueAnimee(images["background"],0,0)
perso = JoueurAnimee(images["luffy"],100,100)

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
        niveau = Niveau("niveau/niveauTest.txt")
        niveau.generer()
        niveau.afficher(fenetre, images["mur"])

        perso.afficher((fenetre))

        perso.Deplacer(touches,x_fen,y_fen, niveau)
        tire, images = perso.shoot(touches, tire, images)
        

        creerballe(touches)
        creerEnnemies(tour,x_fen)
        
        print(len(tire))

        #Afficher et deplacer les éléments d'un tableaux 
        for b in balle:
            b.afficher((fenetre))
            b.Deplacer(x_fen,y_fen)

        for e in ennemies:
            e.afficher((fenetre))
            e.Tombe(x_fen,y_fen)

        for t in tire:
            t.afficher((fenetre))
            t.Tire(x_fen,y_fen)
            
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
            if event.type == pygame.QUIT or touches[K_ESCAPE]:
                continuer = False
pygame.quit()

        
