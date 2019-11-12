import pygame
from pygame.locals import *

cheminInfo = "niveau/level0_info.txt"
cheminNiveau = "niveau/level0.bin"

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
			if data[c] != ' ':
				if i == matW:
					j += 1
					i = -1
				if data[c] != '0' and data[c] != '\n':
					matrice[i][j] = data[c]
				i += 1
			c += 1
	return matrice