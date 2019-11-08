import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from BalleTiree import BalleTiree

class JoueurAnimee(ElementGraphiqueAnimee):
	def __init__(self, img, x = 0, y = 0, mat = [], size = 72):
		ElementGraphiqueAnimee.__init__(self, img["debout"], x, y)
		self.vies = 7
		self.alive = True
		self.boost = 1
		self.cheat = False
		self.time = 0
		self.trigger = 0
		self.timer = False
		self.tps = 0
		self.image = img
		self.numimage = 0
		self.direction = "debout"
		self.tire = []
		self.vitesse = 12
		self.collision = [False, False, False, False] #UP, DOWN, LEFT, RIGTH
		self.taille_tuile = size
		self.matrice = mat

	def verifCollision(self):
		self.collision = [False, False, False, False]
		if self.matrice[int(self.rect.x/self.taille_tuile)][int(self.rect.y/self.taille_tuile)] != "0":
			self.collision[0] = True

		if self.matrice[int(self.rect.x/self.taille_tuile)][int((self.rect.y+self.rect.h)/self.taille_tuile)] != "0":
			self.collision[1] = True

		if self.matrice[int((self.rect.x+self.rect.w)/self.taille_tuile)][int(self.rect.y/self.taille_tuile)] != "0":
			self.collision[2] = True

		if self.matrice[int((self.rect.x-self.rect.w)/self.taille_tuile)][int(self.rect.y/self.taille_tuile)] != "0":
			self.collision[3] = True

	def deplacer(self, touches, window):
		self.verifCollision()
		largeur, hauteur = window.get_size()
		if self.rect.x <= -10 or self.rect.x >= largeur-self.rect.w :
			self.deltaX = - self.deltaX
			self.rect.x = self.rect.x

		if self.rect.y <= 0 or self.rect.y >= hauteur-self.rect.h :
			self.deltaY = - self.deltaY
			self.rect.y = self.rect.y

		if touches[pygame.K_UP]:
			self.direction = "dos"
			self.numimage += 1
			sens = 1
			if self.collision[0]:
				self.rect.y = self.rect.y
			else:
				self.rect.y -= self.vitesse * self.boost

		elif touches[pygame.K_DOWN]:
			self.direction = "face"
			self.numimage += 1
			if  self.collision[1]:
				self.rect.y = self.rect.y
			else:
				self.rect.y += self.vitesse * self.boost

		elif touches[pygame.K_RIGHT]:
			self.direction = "droite"
			self.numimage += 1
			if self.collision[2]:
				self.rect.x = self.rect.x
			else:
				self.rect.x += self.vitesse * self.boost

		elif touches [pygame.K_LEFT]:
			self.direction = "gauche"
			self.numimage += 1
			if self.collision[3]:
				self.rect.x = self.rect.x
			else:
				self.rect.x -= self.vitesse * self.boost
		else:
			self.direction = "debout"

	def Tire(self):
		if(self.direction == "dos"):
			return 0,-10
		elif(self.direction == "face" or self.direction == "debout"):
			return 0,10
		elif(self.direction == "droite"):
			return 10,0
		elif(self.direction == "gauche"):
			return -10,0

	def setTire(self,delta=[]):
		self.tire = delta
		return self.tire

	def afficher(self, window) :
		if (self.fps % 1 )== 0:
			self.numimage = (self.numimage)%len(self.image[self.direction])
			window.blit(self.image[self.direction][self.numimage],self.rect,)

	def recevoirDegats(self):
		self.vies -= 1
		if self.vies <= 0:
			self.alive = False

	def isAlive(self):
		return self.alive

	def recevoirVie(self):
		self.vies += 1

	def Boost(self,tour=0):
		if self.trigger == 1:
			if tour < self.time:
				self.boost = 2 
			else:
				self.trigger = 0
		else:
			self.boost = 1
										 
	def Cheat(self,tour=0):
		if self.trigger == 2:
			if tour < self.time:
				self.boost = 2
				self.cheat = True
			else:
				self.boost = 1
				self.recevoirVie()
				self.cheat = False
				self.trigger = 0
			#Ne prend plus de degats et recois une vie

	def Frame(self,tour,window,images):
		if self.trigger == 3:
			if tour < self.time:
				self.cheat = True
				if (tour%4 == 0):
					self.direction = "hit"
				else:
					self.direction = self.direction
			else:
				self.trigger = 0
				self.cheat = False
				self.recevoirDegats()
		
	def setTime(self,tour,time,num):
		self.time = tour + time
		self.trigger = num
		return self.time

	def shoot(self, touches, event, tire, images):
		if event.type == pygame.KEYUP and event.key == pygame.K_s:
			tire.append(BalleTiree(images["chomp"],self.setTire(self.Tire()),self.rect.x,self.rect.y))
		return tire, images