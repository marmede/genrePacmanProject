import pygame
from pygame.locals import *

cheminInfo = "level0_info.txt"
nomNiveau = "level0.bin"

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
	for i in range(matW):
		temp = []
		for j in range(matH):
			temp.append("0")
		matrice.append(temp)
	if path != "":
		file = open(path, "r")
		data = file.read()
		file.close()
		i, j, c = 0, 0, 0
		while(c < len(data) and j < matH):
			print(data[c], len(data), c, matW, i, matH, j)
			if data[c] != ' ':
				if i == matW:
					j += 1
					i = -1
				if data[c] != '0' and data[c] != '\n':
					matrice[i][j] = data[c]
				i += 1
			c += 1
	return matrice

def enregistrer(data, matW, matH, path):
	text = ""
	file = open(path, "w")
	for j in range(matH):
		for i in range(matW):
			text += matrice[i][j]
			text += ' '
		text += '\n'
	print(text)
	file.write(text)
	file.close()

def ajouterTuile(mat, x, y, matW, matH, size, selection):
	mat[int(x/size)][int(y/size)] = str(selection)
	return matrice

def clearScreen(color):
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
pygame.display.set_caption("Level Generator v1.0")
continuer = 1
winW = 1008
winH = 792
window = pygame.display.set_mode((winW, winH))
nombre_tuile, taille_tuile, chemin_tuiles = chargerInfoTuiles(cheminInfo)
tuiles = chargerImages(chemin_tuiles)

matW = int(winW/taille_tuile) + 1
matH = int(winH/taille_tuile) + 1

matrice = chargerMatrice(matW, matH, "level0.bin")
print(matrice)

selection = -1
print("Pas de tuile sélectionnée.")

color = 'w'
clearScreen(color)

while continuer:
	touches = pygame.key.get_pressed()

	if(touches[pygame.K_1]):
		selection = 1
		print("La tuile 1 est sélectionnée.")
	elif(touches[pygame.K_2]):
		selection = 2
		print("La tuile 2 est sélectionnée.")
	elif(touches[pygame.K_3]):
		selection = 3
		print("La tuile 3 est sélectionnée.")
	elif(touches[pygame.K_4]):
		selection = 4
		print("La tuile 4 est sélectionnée.")
	elif(touches[pygame.K_5]):
		selection = 5
		print("La tuile 5 est sélectionnée.")
	elif(touches[pygame.K_6]):
		selection = 6
		print("La tuile 6 est sélectionnée.")
	elif(touches[pygame.K_7]):
		selection = 7
		print("La tuile 7 est sélectionnée.")
	elif(touches[pygame.K_8]):
		selection = 8
		print("La tuile 8 est sélectionnée.")
	elif(touches[pygame.K_9]):
		selection = 9
		print("La tuile 9 est sélectionnée.")
	elif(touches[pygame.K_0]):
		selection = 10
		print("La tuile 10 est sélectionnée.")

	if(touches[pygame.K_z]):
		clearScreen('w')
		color = 'w'
	elif(touches[pygame.K_c]):
		clearScreen('c')
		color = 'c'
	elif(touches[pygame.K_b]):
		clearScreen('b')
		color = 'b'

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			enregistrer(matrice, matW, matH, nomNiveau)
			continuer = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			if event.button == 1 and selection != -1:
				matrice = ajouterTuile(matrice, x, y, matW, matH, taille_tuile, selection)
			if event.button == 3:
				clearScreen(color)
				matrice = ajouterTuile(matrice, x, y, matW, matH, taille_tuile, 0)

	for i in range(matW):
		for j in range(matH):
			if matrice[i][j] != '0' and selection <= taille_tuile:
				Tuile(tuiles[int(matrice[i][j])-1], i*taille_tuile+1, j*taille_tuile+1).afficher(window)

	pygame.display.flip()

pygame.quit()