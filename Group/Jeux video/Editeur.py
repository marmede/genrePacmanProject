import pygame
from pygame.locals import *

cheminInfo = "niveau/level0_info.txt"
nomNiveau = "niveau/niveauTest.txt"

class Tuile():
	"""Classe représentant une tuile, on ne définit qu'une méthode
	pour afficher la tuile à la position demandée"""
	def __init__(self, img, x, y):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def afficher(self, window):
		window.blit(self.image, self.rect)

def chargerInfoTuiles(path):
	file = open(path, "r") #on ouvre le fichier spécifier pour chager les infos
	data = file.read()

	c = 0
	size = -1
	temp = []
	tiles = []
	nb_tiles = -1
	flag = 0
	l = len(data)

	for i in range(l):
		if data[i] == '\n':
			if c == 0:
				c += 1
				nb_tiles = int("".join(temp))
			elif c == 1:
				c += 1
				size = int("".join(temp))
			elif c > 1:
				tiles.append("".join(temp))
			flag = 0
			temp = []
		elif flag:
			temp.append(data[i])

		if data[i] == ' ':
			if c == 0:
				flag = 1
			elif c == 1:
				flag = 2
			else:
				flag = 3
	tiles.append("".join(temp))

	file.close()
	return (nb_tiles, size, tiles)

def chargerImages(paths):
	tuiles = []
	print(paths)
	for i in range(len(paths)):
		tuiles.append(pygame.image.load(paths[i]).convert_alpha())
	return tuiles

def chargerMatrice(matW, matH, path):
	matrice = []
	fichier = open(path, "r")
	for ligne in fichier:
		l = []
		for i in ligne:
			if i != '\n':
				l.append(int(i))
		matrice.append(l)
	return matrice

def enregistrer(data, matW, matH, path):
	text = ""
	file = open(path, "w")
	for j in range(matH):
		for i in range(matW):
			text += matrice[i][j]
		text += '\n'
	file.write(text)
	file.close()

def ajouterTuile(mat, x, y, matW, matH, size, selection):
	mat[int(x/size)][int(y/size)] = str(selection)
	return mat

def clearScreen(window, color):
	black = [0, 0, 0]
	cyan = [0, 255, 255]
	white = [255, 255, 255]
	if color == 'w':
		window.fill(white)
	elif color == 'c':
		window.fill(cyan)
	elif color == 'b':
		window.fill(black)

pygame.init()
pygame.display.set_caption("Level Editor v1.0")
continuer = 1
winW = 1184
winH = 640
window = pygame.display.set_mode((winW, winH))
nombre_tuile, taille_tuile, chemin_tuiles = chargerInfoTuiles(cheminInfo)
tuiles = chargerImages(chemin_tuiles)

matW = int(winW/taille_tuile) + 1
matH = int(winH/taille_tuile) + 1

matrice = chargerMatrice(matW, matH, nomNiveau)
print(matrice)

selection = -1
print("Pas de tuile sélectionnée.")

color = 'w'
clearScreen(window, color)

while continuer:
	touches = pygame.key.get_pressed()

	if touches[pygame.K_1]:
		selection = 1
		print("La tuile 1 est sélectionnée.")
	elif touches[pygame.K_2]:
		selection = 2
		print("La tuile 2 est sélectionnée.")
	elif touches[pygame.K_3]:
		selection = 3
		print("La tuile 3 est sélectionnée.")
	elif touches[pygame.K_4]:
		selection = 4
		print("La tuile 4 est sélectionnée.")
	elif touches[pygame.K_5]:
		selection = 5
		print("La tuile 5 est sélectionnée.")
	elif touches[pygame.K_6]:
		selection = 6
		print("La tuile 6 est sélectionnée.")
	elif touches[pygame.K_7]:
		selection = 7
		print("La tuile 7 est sélectionnée.")
	elif touches[pygame.K_8]:
		selection = 8
		print("La tuile 8 est sélectionnée.")
	elif touches[pygame.K_9] :
		selection = 9
		print("La tuile 9 est sélectionnée.")
	elif touches[pygame.K_0]:
		selection = 10
		print("La tuile 10 est sélectionnée.")

	if touches[pygame.K_z]:
		clearScreen(window, 'w')
		color = 'w'
	elif touches[pygame.K_c]:
		clearScreen(window, 'c')
		color = 'c'
	elif touches[pygame.K_b]:
		clearScreen(window, 'b')
		color = 'b'

	for event in pygame.event.get():
		if event.type == pygame.QUIT or touches[pygame.K_ESCAPE]:
			enregistrer(matrice, matW, matH, nomNiveau)
			exec(open("main.py").read())
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			if event.button == 1 and selection != -1:
				matrice = ajouterTuile(matrice, x, y, matW, matH, taille_tuile, selection)
			if event.button == 3:
				clearScreen(window, color)
				matrice = ajouterTuile(matrice, x, y, matW, matH, taille_tuile, 0)

	for i in range(matW):
		for j in range(matH):
			if matrice[i][j] != 0 and selection <= taille_tuile:
				Tuile(tuiles[int(matrice[i][j])-1], i*taille_tuile+1, j*taille_tuile+1).afficher(window)

	pygame.display.flip()
