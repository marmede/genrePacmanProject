import pygame
from pygame.locals import *
from ElementGraphique import ElementGraphique

def menuGameOver(score, font, x_fen, y_fen, touches, fenetre, text, etat, continuer):
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