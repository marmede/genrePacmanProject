import pygame
from pygame.locals import *
from ElementGraphique import ElementGraphique
from ElementGraphiqueAnimee import ElementGraphiqueAnimee

def menuJeu(fenetre, blur, x_fen, y_fen, sTxt, menuFont, menuTxt):
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
			if click[0]:
				return menuTxt[i]
			offsetColor = blue
		#sinon on remet la couleur d'avant
		else:
			offsetColor = blue
	return ""