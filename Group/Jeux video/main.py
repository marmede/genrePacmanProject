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
from Menu import *

def resizeImgTab(tab, largeur, hauteur):
        newTab =[]
        for img in tab:
                img = pygame.transform.scale(img, (largeur,hauteur))
                newTab.append(img)

        return newTab

def resizeImg(tab, numImg, largeur, hauteur):
        tab[numImg] = pygame.transform.scale(tab[numImg], (largeur,hauteur))
        return tab

def lireImages():
        images = {}
        images["blur"] = [pygame.image.load("images/blur.png").convert_alpha()]
        images["balle"] = [pygame.image.load("images/balle.png").convert_alpha()]
        images["background"] = [pygame.image.load("images/background2.jpg").convert()]
        images["chomp"] = [pygame.image.load("images/Balle/chomp1.png").convert_alpha()]
        images["chomp"] = resizeImgTab(images["chomp"], 16, 16)
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
        images["mur"].append(pygame.image.load("images/black-hole.png").convert_alpha())
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

        images["blinky"]["droite"] = []
        images["blinky"]["droite"].append(pygame.image.load("images/Fantomes/Blinky/blinky-d-1.png").convert_alpha())
        images["blinky"]["droite"].append(pygame.image.load("images/Fantomes/Blinky/blinky-d-2.png").convert_alpha())

        images["blinky"]["debout"] = resizeImgTab(images["blinky"]["debout"], 16, 16)
        images["blinky"]["haut"] = resizeImgTab(images["blinky"]["haut"], 16, 16)
        images["blinky"]["bas"] = resizeImgTab(images["blinky"]["bas"], 16, 16)
        images["blinky"]["gauche"] = resizeImgTab(images["blinky"]["gauche"], 16, 16)
        images["blinky"]["droite"] = resizeImgTab(images["blinky"]["droite"], 16, 16)
        return images

def chargerNiveau(i_niv, niveaux, y_fen, x_fen, img):
    print(i_niv)
    niveau = Niveau(niveaux[i_niv],img)
    niveau.createLab(y_fen,x_fen,img[0].get_height(),img[0].get_width())
    creerballe(niveau,fenetre, img[4])
    creerEnnemies(niveau)
    return niveau, i_niv

def creerballe(niveau,fenetre, img):
        i = 0
        for y in range(len(niveau.tab)):
                for x in range(len(niveau.tab[y])):
                        if niveau.tab[y][x] == 0:
                                if (i%2) == 0:
                                        balle.append(ElementGraphique(images["balle"][0],(32 * x)+8,(32 * y)+8))
                                i += 1
                        if niveau.tab[y][x] == 4:
                                trou.append(ElementGraphique(img, (32*x), (32*y)))

        
def creerEnnemies(niveau):
        i = 0
        for y in range(len(niveau.tab)):
                for x in range(len(niveau.tab[y])):
                        if niveau.tab[y][x] == 0:
                                if (i%452) == 0:
                                        ennemies.append(Fantome(images["blinky"],(32 * x)+8,(32 * y)+8))
                                i += 1

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
        fichier = open("niveau/score.txt","a")  
        fichier.seek(0)
        fichier.write(text+" "+str(score)+'\n') 
        fichier.truncate() 
        fichier.close()

def lireScore():  
    fichier = open("niveau/score.txt","r")  
    data = fichier.read()  
  
    data = data.split("\n")  
    data.sort() 
    return data

def recommencer(perso, score, niveau, ennemies):
        perso.rect.x = 2*32
        perso.rect.y = 3*32
        i = 0
        for y in range(len(niveau.tab)):
                for x in range(len(niveau.tab[y])):
                        if niveau.tab[y][x] == 0:
                                if (i%4) == 0:
                                        balle.append(ElementGraphique(images["balle"][0],(32 * x)+8,(32 * y)+8))
                                i += 1
        score = 0
<<<<<<< HEAD
        return perso, score

def lireScore(): 
    fichier = open("niveau/score.txt","r") 
    data = fichier.read() 
    fichier.close()
    return data[:len(data)-1]

def sauverScore(score): 
    fichier = open("niveau/score.txt","w")
    fichier.write(str(score)+'\n')
    fichier.close() 
=======
        creerEnnemies(niveau)
        return perso, score, ennemies

def fauxBalles(tab):
        for e in tab:
                e.alive = False
        return tab
>>>>>>> master

def changerSon(n):
        pygame.mixer.stop()
        n.play()

pygame.init()
x_fen = 1184
y_fen = 640
fenetre = pygame.display.set_mode((x_fen,y_fen))
#pygame.display.set_mode((0,0),pygame.FULLSCREEN)

images = lireImages()
sTxt = 72

menuFont = pygame.font.Font(None, sTxt)  
menuTxt = ["JOUER", "MEILLEUR SCORE", "EDITEUR NIVEAU", "QUITTER"] 
topScore = lireScore()  
topScore.append("RETOUR") 
 
dicoMenu = {"menu": menuTxt, "classement": topScore} 

#Les tableaux des éléments
balle = []
trou = []
ennemies = []
tire=[]
tiles=[]
ghost = None

font = pygame.font.Font(None, 34)
<<<<<<< HEAD
menuFont = pygame.font.Font(None, sTxt) 
menuTxt = ["JOUER", "MEILLEUR SCORE", "EDITEUR NIVEAU", "QUITTER"]
topScore = [lireScore()]
topScore.append("RETOUR")

dicoMenu = {"menu": menuTxt, "classement": topScore}
=======
>>>>>>> master

images["blur"] = resizeImgTab(images["blur"], x_fen, y_fen)
blur = ElementGraphiqueAnimee(images["blur"], 0, 0)
images["mur"] = resizeImg(images["mur"], 4, 30, 30)
fond = ElementGraphiqueAnimee(images["background"],0,0)
perso = JoueurAnimee(images["luffy"], 32*2, 32*3)
i_niv = 0
niveaux = ["niveau/niveauTest.txt", "niveau/niveauTest2.txt"]
niveau, i_niv = chargerNiveau(i_niv, niveaux, x_fen, y_fen, images["mur"])

game_over = False
key_up = True
touch_wait = pygame.time.get_ticks()
continuer = 1

sonMenu = pygame.mixer.Sound("musiques/awesomeness.wav")
sonNiveau1 = pygame.mixer.Sound("musiques/awake10.ogg")

#Tour == variable de temps
tour = 0
pos= []
score = 0

etat = "menu"

text = ''

changementSon = True

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

        if etat == "menu":
                etat, dicoMenu = menuJeu(fenetre, etat, blur, x_fen, y_fen, sTxt, menuFont, dicoMenu)

        if etat == "jeu":
                if changementSon:
                        changerSon(sonNiveau1)
                        changementSon = False
                niveau.afficherLab(images["mur"],fenetre)
                perso.afficher(fenetre)
                perso.deplacer(niveau,touches, fenetre)
                #Afficher et deplacer les éléments d'un tableaux 
                for b in balle:
                        b.afficher(fenetre)
                        if b.collide(perso):
                                score += 1
                        # b.Deplacer(x_fen, y_fen)

                for t in trou:
                        t.afficher(fenetre)
                        if t.collide(perso):
                                if i_niv+1 < 2:
                                        balle = fauxBalles(balle)
                                        balle = supprimerElements(balle)
                                        niveau, i_niv = chargerNiveau(i_niv+1, niveaux, x_fen, y_fen, images["mur"])
                                else:
                                        etat = "win"
                                        i_niv = 0
                                        niveau, i_niv = chargerNiveau(i_niv+1, niveaux, x_fen, y_fen, images["mur"])
                                trou = supprimerElements(trou)

                for t in tiles:
                        t.afficher(fenetre)

                for e in ennemies:
                        e.afficher(fenetre)
<<<<<<< HEAD
                        if e.collide(perso):
                            perso.alive = False
                        if e.deplacer(niveau, fenetre, perso.rect.x, perso.rect.y):
                            perso.alive = False

                for t in tire:
                        t.afficher(fenetre)
=======
>>>>>>> master
                        e.deplacer(niveau, fenetre, perso.rect.x, perso.rect.y,)
                        if perso.collide(e):
                                etat = "perdu"
                                test = ''
                                changementSon = True

                for t in tire:
                        t.afficher(fenetre)
                        t.Colli(niveau)
                        for e in ennemies:
                            if t.collide(e):
                                e.alive = False
                        t.Tire(x_fen, y_fen)


                scoreEcran = "Score: {}".format(score)
                scoreMenu = ElementGraphique(font.render(scoreEcran, True, (255, 255, 0)), x_fen/2-70, 30)
                scoreMenu.afficher(fenetre)
                ######################################
                if perso.PixToCase(niveau) == 3:
                        print("push")

<<<<<<< HEAD
                if not perso.isAlive():
=======
                if touches[pygame.K_ESCAPE]:
                        etat = "pause"
                        text = ''
                        changementSon = True

        if etat == "pause":
                etat = menuPositionJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, menuTxt)
        if etat == "win":
                if changementSon:
                        changerSon(sonMenu)
                        changementSon = False
                etat, text, continuer = menuWin(scoreMenu, font, x_fen, y_fen, touches, fenetre, text, etat, continuer)
                Enregistrer(score, text)

        if etat == "perdu":
                if changementSon:
                        changerSon(sonMenu)
                        changementSon = False
                score, etat, continuer = menuGameOver(score, font, touches, fenetre, etat, continuer)

        if etat == "recommencer":
                ennemies = []
                perso, score, ennemies = recommencer(perso, score, niveau, ennemies)
                etat = "menu"
                changementSon = True

        ######################################

        #Suppressions des éléments inutiles (mort ou hors écran)
        balle = supprimerElements(balle) #on gagne
        ennemies = supprimerElements(ennemies) #on perd point
        tire = supprimerElements(tire)

        pygame.display.flip()

        for event in pygame.event.get():
<<<<<<< HEAD
            tire, images, score = perso.shoot(touches, event, tire, images, score)
            if event.type == pygame.QUIT or etat == "quitter":
                    continuer = 0
        if continuer == 0 and score > int(topScore[0]):
            sauverScore(score)
=======
                tire, images, score = perso.shoot(touches, event, tire, images, score)
                if event.type == pygame.QUIT or etat == "quitter":
                        continuer = 0
>>>>>>> master

pygame.quit()