import pygame
from pygame.locals import *
from ElementGraphique import ElementGraphique

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
		perdu = "Ta perdu c:"
		perduImg = ElementGraphique(font.render(perdu, True, (255,255,255)), largeur/2-105, hauteur/2)
		perduImg.afficher(fenetre)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				continuer = 0

	score = 0
	return score, etat, continuer