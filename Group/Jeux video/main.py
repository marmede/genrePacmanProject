import pygame
import random
from pygame.locals import *
from random import randint
from ElementGraphique import ElementGraphique
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from JoueurAnimee import JoueurAnimee
from BalleAnimee import BalleAnimee
from BonusAnimee import BonusAnimee
from BalleTiree import BalleTiree
from Niveau import *
from Fantome import Fantome
from GameOver import *

def resizeImgTab(tab, largeur, hauteur):
        newTab =[]
        for img in tab:
                img = pygame.transform.scale(img, (largeur,hauteur))
                newTab.append(img)

        return newTab

def resizeImg(tab, numImg, largeur, hauteur):
        compt = 0
        newTab =[]
        for img in tab:
                compt +=1
                if compt == numImg:
                        img = pygame.transform.scale(img, (largeur,hauteur))
                newTab.append(img)

        return newTab

def lireImages():
        images = {}
        images["blur"] = [pygame.image.load("images/blur.png").convert_alpha()]
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
        images["luffy"]["gauche_s"] = []
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-1.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-2.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-3.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-4.png").convert_alpha())
        images["luffy"]["gauche"].append(pygame.image.load("images/Luffy/row-2-col-5.png").convert_alpha())
        images["luffy"]["gauche_s"].append(pygame.image.load("images/Luffy/row-2-col-1.png").convert_alpha())

        images["luffy"]["droite"] = []
        images["luffy"]["droite_s"] = []
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-1.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-2.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-3.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-4.png").convert_alpha())
        images["luffy"]["droite"].append(pygame.image.load("images/Luffy/row-3-col-5.png").convert_alpha())
        images["luffy"]["droite_s"].append(pygame.image.load("images/Luffy/row-3-col-1.png").convert_alpha())

        images["luffy"]["dos"] = []
        images["luffy"]["dos_s"] = []
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-1.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-2.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-3.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-4.png").convert_alpha())
        images["luffy"]["dos"].append(pygame.image.load("images/Luffy/row-4-col-5.png").convert_alpha())
        images["luffy"]["dos_s"].append(pygame.image.load("images/Luffy/row-4-col-1.png").convert_alpha())

        images["mur"] = []
        images["mur"].append(pygame.image.load("images/Mur/bois.png"))
        images["mur"].append(pygame.image.load("images/Mur/brique.png"))
        images["mur"].append(pygame.image.load("images/Mur/eau.png"))
        images["mur"].append(pygame.image.load("images/Mur/mur.png"))
        #images["mur"].append(pygame.image.load("images/Mur/"))


        images["blinky"] = {}

        images["blinky"]["debout"] = [pygame.image.load("images/Fantomes/Blinky/blinky-b-1.png").convert_alpha()]

        images["blinky"]["haut"] = []
        images["blinky"]["haut"].append(pygame.image.load("images/Fantomes/Blinky/blinky-t-1.png").convert_alpha())
        images["blinky"]["haut"].append(pygame.image.load("images/Fantomes/Blinky/blinky-t-2.png").convert_alpha())

        images["blinky"]["bas"] = []
        images["blinky"]["bas"].append(pygame.image.load("images/Fantomes/Blinky/blinky-b-1.png").convert_alpha())
        images["blinky"]["bas"].append(pygame.image.load("images/Fantomes/Blinky/blinky-b-2.png").convert_alpha())

        images["blinky"]["gauche"] = []
        images["blinky"]["gauche"].append(pygame.image.load("images/Fantomes/Blinky/blinky-l-1.png").convert_alpha())
        images["blinky"]["gauche"].append(pygame.image.load("images/Fantomes/Blinky/blinky-l-2.png").convert_alpha())

        images["blinky"]["droit"] = []
        images["blinky"]["droit"].append(pygame.image.load("images/Fantomes/Blinky/blinky-d-1.png").convert_alpha())
        images["blinky"]["droit"].append(pygame.image.load("images/Fantomes/Blinky/blinky-d-2.png").convert_alpha())

        images["blinky"]["debout"] = resizeImgTab(images["blinky"]["debout"], 30, 30)
        images["blinky"]["haut"] = resizeImgTab(images["blinky"]["haut"], 30, 30)
        images["blinky"]["bas"] = resizeImgTab(images["blinky"]["bas"], 30, 30)
        images["blinky"]["gauche"] = resizeImgTab(images["blinky"]["gauche"], 30, 30)
        images["blinky"]["droit"] = resizeImgTab(images["blinky"]["droit"], 30, 30)
        return images

def creerballe(niveau,fenetre):
        i = 0
        for y in range(len(niveau.tab)):
                for x in range(len(niveau.tab[y])):
                        if niveau.tab[y][x] == 0:
                                if (i%2) == 0:
                                        balle.append(ElementGraphique(images["balle"][0],(32 * x)+8,(32 * y)+8))
                                i += 1
        

#def creerEnnemies(tour,x):
#        if (tour%20) == 0:
#                ennemies.append(BalleAnimee(images["balle"],0,-30))

def supprimerElements(tab):
        newTab = []
        for e in tab:
                if e.isAlive():
                        newTab.append(e)
        return newTab

def supprimerElements2D(tab):
        tab = []
        for y in range(len(tab)):
                l = []
                for x in range(len(tab[y])):
                        if tab[y][x].isAlive():
                                l.append(tab[y][x])
                l.append(tab)
        return tab

def Enregistrer(score,text):
        fichier = open("score.txt","w")
        fichier.write(text+ " "+ str(score))
        fichier.close


pygame.init()
x_fen = 1184
y_fen = 640
fenetre = pygame.display.set_mode((x_fen,y_fen))
#pygame.display.set_mode((0,0),pygame.FULLSCREEN)

images = lireImages()

#Les tableaux des éléments
balle = []
ennemies = []
tire=[]
tiles=[]
ghost = None

font = pygame.font.Font(None, 34)

blur = ElementGraphiqueAnimee(images["blur"], 0, 0)
images["blur"] = resizeImgTab(images["blur"], x_fen, y_fen)
images["mur"] = resizeImg(images["mur"], 4, 30, 30)
fond = ElementGraphiqueAnimee(images["background"],0,0)
perso = JoueurAnimee(images["luffy"], 32*2, 32*3)
niveau = Niveau("niveau/niveauTest.txt",images["mur"])
niveau.createLab(y_fen,x_fen,images["mur"][0].get_height(),images["mur"][0].get_width())
creerballe(niveau,fenetre)

game_over = False
key_up = True
touch_wait = pygame.time.get_ticks()
continuer = 1

#Tour == variable de temps
tour = 0
pos= []
score = 0

etat = "jeu"

text = ''


while continuer:
        tour += 1
        framerate = pygame.time.Clock()
        Fps = framerate.tick(35)
        #Affichage images
        fond.afficher(fenetre)
        #Atribution des touches
        touches = pygame.key.get_pressed()
        #Attribution de la souris et de son click
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        print(niveau.tab[2][2])
        
        if etat == "jeu":
                niveau.afficherLab(images["mur"],fenetre)
                perso.afficher(fenetre)
                perso.deplacer(niveau,touches, fenetre)
                score += 1
                #Afficher et deplacer les éléments d'un tableaux 
                for b in balle:
                        b.afficher(fenetre)
                        # b.Deplacer(x_fen, y_fen)

                for t in tiles:
                        t.afficher(fenetre)

                for e in ennemies:
                        e.afficher(fenetre)
                        #e.Tombe(x_fen, y_fen)
                        if e.collide(perso):
                                score += 1

                for t in tire:
                        t.afficher(fenetre)
                        t.Tire(x_fen, y_fen)

                ######################################
                if perso.PixToCase(niveau) == 3:
                        print("push")

                if perso.isAlive() == False or touches[pygame.K_ESCAPE]:
                        etat = "perdu"
                        text = ''
        if etat == "perdu":
                etat, text, continuer = menuGameOver(score, font, x_fen, y_fen, touches, fenetre, text, etat, continuer)
                Enregistrer(score, text)

        ######################################

        #Suppressions des éléments inutiles (mort ou hors écran)
        balle = supprimerElements(balle) #on gagne
        ennemies = supprimerElements(ennemies) #on perd point
        tire = supprimerElements(tire)

        pygame.display.flip()

        for event in pygame.event.get():
                # tire, images = perso.shoot(touches, event, tire, images)
                if event.type == pygame.QUIT:
                        continuer = 0

pygame.quit()


        # print("HAUT")
        # print(perso.PixToCase(niveau,0,24,0,-1))
        # print(perso.PixToCase(niveau,14,24,0,-1))
        # print("BAS")
        # print(perso.PixToCase(niveau,0,0,0,1))
        # print(perso.PixToCase(niveau,14,0,0,1))
        # print("GAUCHE")
        # print(perso.PixToCase(niveau,24,0,-1,0))
        # print(perso.PixToCase(niveau,24,16,-1,0))
        # print("DROITE")
        # print(perso.PixToCase(niveau,-16,0,1,0))
        # print(perso.PixToCase(niveau,-16,16,1,0))