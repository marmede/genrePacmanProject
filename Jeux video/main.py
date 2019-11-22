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
from Menu import *
from Fantome import Fantome

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
<<<<<<< HEAD
	images = {}
	images["blur"] = [pygame.image.load("images/blur.png").convert_alpha()]
	images["balle"] = [pygame.image.load("images/balle.png").convert_alpha()]
	images["balle"] = resizeImgTab(images["balle"], 45, 45)
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

	images["blinky"]["debout"] = resizeImgTab(images["blinky"]["debout"], 50, 50)
	images["blinky"]["haut"] = resizeImgTab(images["blinky"]["haut"], 50, 50)
	images["blinky"]["bas"] = resizeImgTab(images["blinky"]["bas"], 50, 50)
	images["blinky"]["gauche"] = resizeImgTab(images["blinky"]["gauche"], 50, 50)
	images["blinky"]["droit"] = resizeImgTab(images["blinky"]["droit"], 50, 50)
	return images

def creerballe(touches):
	if touches[K_SPACE]:
		balle.append(BalleAnimee(images["luffy"]["debout"]))

def creerEnnemies(tour,x):
		if (tour%20) == 0:
				ennemies.append(BalleAnimee(images["balle"],0,-50))
=======
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
>>>>>>> master

def supprimerElements(tab):
	newTab = []
	for e in tab:
		if e.isAlive():
			newTab.append(e)
	return newTab

<<<<<<< HEAD
<<<<<<< HEAD
def lireScore():
	fichier = open("niveau/score.txt","r")
	data = fichier.read()

	data = data.split("\n")
	data.sort()

	fichier.close()
	return data[1:6]

def sauverScore(score):
	fichier = open("niveau/score.txt","a")
	fichier.write(str(score)+'\n')
	fichier.close()

=======
>>>>>>> master
=======
def supprimerElements2D(tab):
        tab = []
        for y in range(len(tab)):
                l = []
                for x in range(len(tab[y])):
                        if tab[y][x].isAlive():
                                l.append(tab[y][x])
                l.append(tab)
        return tab

>>>>>>> master

pygame.init()
x_fen = 1184
y_fen = 640
fenetre = pygame.display.set_mode((x_fen,y_fen))
#pygame.display.set_mode((0,0),pygame.FULLSCREEN)

<<<<<<< HEAD
nombre_tuile, taille_tuile, chemin_tuiles = chargerInfoTuiles(cheminInfo)
tuiles = chargerImages(chemin_tuiles)
#tuiles = resizeImg(tuiles, 5, 72, 72)
matW = int(x_fen/taille_tuile) + 1
matH = int(y_fen/taille_tuile) + 1

matrice = chargerMatrice(matW, matH, cheminNiveau)
#print(matrice)

score = 0
yellow = (255, 255, 0)
font = pygame.font.Font(None, 34)
sTxt = 72
menuFont = pygame.font.Font(None, sTxt)
menuTxtFR = ["JOUER", "CLASSEMENT", "EDITEUR NIVEAU", "OPTIONS", "QUITTER"]
menuTxtES = ["JUGAR", "CLASIFICACIÓN", "EDITOR DE NIVEL", "OPCIONES", "SALIR"]
menuTxtEN = ["PLAY", "RANKING", "LEVEL EDITOR", "OPTIONS", "EXIT"]
menuTxt = menuTxtFR
optionTxt = ["FRANCAIS", "ESPANOL", "ENGLISH", "RETOUR"]
topScore = lireScore()
topScore.append("RETOUR")
print(topScore)
dicoMenu = {"menu": menuTxt, "options": optionTxt, "classement": topScore, "fr": menuTxtFR, "en": menuTxtEN, "es": menuTxtES}

images = lireImages();
=======
images = lireImages()

>>>>>>> master
#Les tableaux des éléments
balle = []
ennemies = []
tire=[]
tiles=[]
ghost = None



blur = ElementGraphiqueAnimee(images["blur"], 0, 0)
images["blur"] = resizeImgTab(images["blur"], x_fen, y_fen)
fond = ElementGraphiqueAnimee(images["background"],0,0)
perso = JoueurAnimee(images["luffy"], 32*2, 32*3)
niveau = Niveau("niveau/niveauTest.txt",images["mur"])
niveau.createLab(y_fen,x_fen,images["mur"][0].get_height(),images["mur"][0].get_width())
creerballe(niveau,fenetre)

game_over = False
key_up = True
touch_wait = pygame.time.get_ticks()
continuer = True
etat = "menu"

#Tour == variable de temps
tour = 0
<<<<<<< HEAD

for i in range(matW):
	for j in range(matH):
		if matrice[i][j] != '0':
			tiles.append(Tuile(tuiles[int(matrice[i][j])-1], i*taille_tuile+1, j*taille_tuile+1))
		else:
			#print("ghost :", ghost)
			if not(ghost):
				ghost = Fantome(images["blinky"], i*taille_tuile+1,j*taille_tuile+1, matrice, taille_tuile)
			ennemies.append(Tuile(tuiles[int(matrice[i][j])-1], i*taille_tuile+1, j*taille_tuile+1))
=======
pos= []
>>>>>>> master

while continuer:
<<<<<<< HEAD
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
	#print(perso.collision)
	#print("POSITION ACTUEL EN X: "+str(perso.rect.x))
	#print("POSITION ACTUEL EN Y: "+str(perso.rect.y))
	# # print("A ne pas depasser : "+str(perso.limite[3]))
	#print(perso.limite)

	#304 376
	if not touches[pygame.K_ESCAPE]:
		key_up = True
	if touches[pygame.K_ESCAPE] and pygame.time.get_ticks() - touch_wait > 300 and key_up:
		key_up = False
		etat = "jeu" if etat == "menu" else "menu"
		touch_wait = pygame.time.get_ticks()


	for t in tiles:
		t.afficher(fenetre)

	if not ennemies:
		for i in range(matW):
			for j in range(matH):
				if matrice[i][j] == '0':
					ennemies.append(Tuile(tuiles[int(matrice[i][j])-1], i*taille_tuile+1, j*taille_tuile+1))

	if etat == "jeu":
		perso.deplacer(touches, fenetre)

		creerballe(touches)
		#creerEnnemies(tour, x_fen)

		perso.afficher(fenetre)

		#print("ghost : ", ghost, ghost[0].rect)
		perso.deplacer(touches, fenetre)

		creerballe(touches)
		creerEnnemies(tour, x_fen)

		#Afficher et deplacer les éléments d'un tableaux 
		for b in balle:
			b.afficher(fenetre)
			b.Deplacer(x_fen, y_fen)

		for e in ennemies:
			e.afficher(fenetre)
			if e.collide(perso):
				score += 1

		for t in tire:
			t.afficher(fenetre)
			t.Tire(x_fen, y_fen)

		#Mort du perso
		if perso.isAlive() == False:
			game_over = True

		scoreTxt = "Score: {}".format(score)
		ElementGraphique(font.render(scoreTxt, True, yellow), (x_fen-(font.size(scoreTxt))[0]) / 2, 20).afficher(fenetre)
	elif etat == "menu" or etat == "options" or etat == "classement":
		etat, dico = menuJeu(fenetre, etat, blur, x_fen, y_fen, sTxt, menuFont, dicoMenu)
	elif etat == "editeur":
		exec(open("Editeur.py").read())

	######################################

	######################################

	#Suppressions des éléments inutiles (mort ou hors écran)
	balle = supprimerElements(balle) #on gagne
	ennemies = supprimerElements(ennemies) #on perd point
	tire = supprimerElements(tire)

	pygame.display.flip()

	for event in pygame.event.get():
		tire, images = perso.shoot(touches, event, tire, images)
		if event.type == pygame.QUIT or etat == "quitter":
			continuer = 0
	if continuer == 0:
		sauverScore(score)
=======
        tour += 1
        framerate = pygame.time.Clock()
        Fps = framerate.tick(35)
        #Affichage images
        fond.afficher(fenetre)
        niveau.afficherLab(images["mur"],fenetre)
        perso.afficher(fenetre)
        #Atribution des touches
        touches = pygame.key.get_pressed()
        #Attribution de la souris et de son click
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        perso.deplacer(niveau,touches, fenetre)

        print(niveau.tab[2][2])
        
        #Afficher et deplacer les éléments d'un tableaux 
        for b in balle:
                b.afficher(fenetre)
                # b.Deplacer(x_fen, y_fen)
                if b.collide(perso):
                        print("ok")

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

        #Mort du perso
        if perso.isAlive() == False:
                game_over = True

        ######################################
        if perso.PixToCase(niveau) == 3:
                print("push")

        ######################################

        #Suppressions des éléments inutiles (mort ou hors écran)
        balle = supprimerElements(balle) #on gagne
        ennemies = supprimerElements(ennemies) #on perd point
        tire = supprimerElements(tire)

        pygame.display.flip()

        for event in pygame.event.get():
                tire, images = perso.shoot(touches, event, tire, images)
                if event.type == pygame.QUIT:
                        continuer = 0
>>>>>>> master

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