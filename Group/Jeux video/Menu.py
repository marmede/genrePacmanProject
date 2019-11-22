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

def menuJeu(fenetre, etat, attendre, blur, x_fen, y_fen, sTxt, menuFont, dico):
	if etat == "menu":
		retour = menuPositionJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, dico["menu"])
		if retour == dico["menu"][0]:
			etat = "jeu"
		elif retour == dico["menu"][1]:
			etat = "classement"
		elif retour == dico["menu"][2]:
			etat = "editeur"
		elif retour == dico["menu"][3]:
			etat = "options"
		elif retour == dico["menu"][4]:
			etat = "quitter"
	elif etat == "options":
		attendre = pygame.time.get_ticks()
		retour = menuPositionJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, dico["options"])
		if retour == "FRANÇAIS":
			dico["options"][3] = "RETOUR"
			dico["menu"] = dico["fr"]
			etat = "menu"
		elif retour == "ESPAÑOL":
			dico["options"][3] = "VOLVER" 
			dico["menu"] = dico["es"]
			etat = "menu"
		elif retour == "ENGLISH":
			dico["options"][3] = "BACK"
			dico["menu"] = dico["en"]
		elif retour == dico["options"][3] and pygame.time.get_ticks() - attendre > 300:
			etat = "menu"
			attendre = pygame.time.get_ticks()
	elif etat == "classement":
		attendre = pygame.time.get_ticks()
		retour = menuPositionJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, dico["classement"])
		if retour == "RETOUR" and pygame.time.get_ticks() - attendre > 300:
			etat = "menu"
			attendre = pygame.time.get_ticks()
	return etat, dico, attendre