import pygame
from pygame.locals import *
from ElementGraphique import ElementGraphique

def menuGameOver(score, font, x_fen, y_fen, touches, fenetre, text, etat):
	print("oui")
	scoreEcran = "Score: {}".format(score)
	scoreMenu = ElementGraphique(font.render(scoreEcran, True, (255, 255, 0)), x_fen/2-70, y_fen/2-70)
	print("non par contre")
	scoreMenu.afficher(fenetre)
	print("mais bon")
	if touches[pygame.K_RETURN]:
		etat = "jouer"
	else:
		entrerMenu = "Entre un pseudo : "
		entrerMenuImg = ElementGraphique(font.render(entrerMenu, True, (255,255,255)), x_fen/2-205, y_fen/2)
		entrerMenuImg.afficher(fenetre)
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key != K_RETURN:
				print("bando hein")
				text += event.unicode
				print("binks")
	fenetre.blit(font.render(text, True, (255, 255, 255)), (x_fen/2, y_fen/2))

	return etat, text