import pygame
from pygame.locals import *
from ElementGraphique import ElementGraphique
from ElementGraphiqueAnimee import ElementGraphiqueAnimee

def menuPositionJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, menuTxt):
	blur.afficher(fenetre)
	click = pygame.mouse.get_pressed()
	mouse = pygame.mouse.get_pos()
	red = (255, 0, 0)
	blue = (0, 0, 255)
	yellow = (255, 255, 0)
	white = (255, 255, 255)
	offsetColor = blue
	textColor = white
	offset = 2

	s = len(menuTxt)
	for i in range(s):
		wTxt, hTxt = menuFont.size(menuTxt[i])
		xTxt = (x_fen - wTxt) / 2
		yTxt = y_fen/2 + (i-int(s/2))*(hTxt+sTxt)
		menuOmbre = ElementGraphique(menuFont.render(menuTxt[i], True, offsetColor), xTxt+offset, yTxt+offset)
		menuOmbre.afficher(fenetre)
		menu = ElementGraphique(menuFont.render(menuTxt[i], True, textColor), xTxt, yTxt)
		#si le text est en collision avec la position de la souris
		if menu.rect.collidepoint(mouse):
			menu.afficher(fenetre)
			offsetColor = blue
			if click[0]:
				return menuTxt[i]
		#sinon on remet la couleur d'avant
		else:
			offsetColor = blue
	return ""

def menuJeu(fenetre, etat, blur, x_fen, y_fen, sTxt, menuFont, dico):
	if etat == "menu":
		retour = menuPositionJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, dico["menu"])
		if retour == dico["menu"][0]:
			etat = "jeu"
		elif retour == dico["menu"][1]:
			etat = "classement"
		elif retour == dico["menu"][2]:
			etat = "editeur"
		elif retour == dico["menu"][3]:
			etat = "quitter"
	elif etat == "classement":
		retour = menuPositionJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, dico["classement"])
		if retour == "RETOUR":
			touch_wait = pygame.time.get_ticks()
			etat = "menu"
			while(pygame.time.get_ticks() - touch_wait < 200):
				continue
	return etat, dico

def menuWin(score, font, x_fen, y_fen, touches, fenetre, text, etat, continuer):
	score.rect.x = x_fen/2-70
	score.rect.y = y_fen/2-70
	score.afficher(fenetre)
	if touches[pygame.K_RETURN]:
		etat = "recommencer"
	else:
		entrerMenu = "Entre un pseudo : "
		entrerMenuImg = ElementGraphique(font.render(entrerMenu, True, (255,255,255)), x_fen/2-205, y_fen/2)
		entrerMenuImg.afficher(fenetre)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				continuer = 0
			if event.type == KEYDOWN and event.key != K_RETURN:
				text += event.unicode
		fenetre.blit(font.render(text, True, (255, 255, 255)), (x_fen/2, y_fen/2))

	return etat, text, continuer

def menuGameOver(score, font, touches, fenetre, etat, continuer):
	largeur, hauteur = fenetre.get_size()
	if touches[pygame.K_RETURN]:
		etat = "recommencer"
	else:
		perdu = "Tu as perdu: "
		perduImg = ElementGraphique(font.render(perdu, True, (255,255,255)), largeur/2-105, hauteur/2)
		perduImg.afficher(fenetre)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				continuer = 0

	score = 0
	return score, etat, continuer