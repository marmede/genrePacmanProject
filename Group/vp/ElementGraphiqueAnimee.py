import pygame
import random
from random import randint
from ElementGraphique import ElementGraphique

class ElementGraphiqueAnimee(ElementGraphique):
	# Le constructeur basique
	def __init__(self, img=[],x=0,y=0,effect=None) :
		self.image = img
		self.fps = 0
		self.numimage = 0
		self.deltaX = 10
		self.deltaY = 10
		self.rect = self.image[self.numimage].get_rect()
		self.rect.x = x
		self.rect.y = y
		self.alive = True
		self.effect = effect

	def afficher(self, window) :
		self.fps += 1
		if (self.fps % 1 )== 0:
			self.numimage = (self.numimage + 1)%len(self.image)
			window.blit(self.image[self.numimage],self.rect)

	def Deplacer(self, window):
		largeur, hauteur = window.get_size()
		self.rect.x += self.deltaX
		if self.rect.x <= -10 or self.rect.x >= largeur-self.rect.w :
			self.deltaX = - self.deltaX
			self.rect.x = self.rect.x

		self.rect.y += self.deltaY
		if self.rect.y <= 0 or self.rect.y >= hauteur-self.rect.h :
			self.deltaY = - self.deltaY
			self.rect.y = self.rect.y