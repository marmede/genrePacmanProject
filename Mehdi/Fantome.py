import pygame
from random import randint
from ElementGraphiqueAnimee import ElementGraphiqueAnimee

class Fantome(ElementGraphiqueAnimee):
    def __init__(self,img,x,y):
        ElementGraphiqueAnimee.__init__(self,img["debout"],x,y)
        
        self.image = img
        self.numimage = 0
        self.direction = "debout"
        self.deltaX = randint(-5, 5)
        self.deltaY = randint(-5, 5)
        self.rect.x = randint(0, 650)
        self.rect.y = randint(10,400)

    def afficher(self, window):
        self.numimage += 1
        if (self.fps % 30 )== 0:
            self.numimage = (self.numimage)%len(self.image[self.direction])
            window.blit(self.image[self.direction][self.numimage],self.rect)

    def Deplacer(self, fenetre):
        largeur, hauteur = fenetre.get_size()

        if self.deltaX > 0:
            self.direction = "droit"
        else:
            self.direction = "gauche"
            
        if self.deltaY > 0:
            self.direction = "bas"
        else:
            self.direction = "haut"

        self.rect.x += self.deltaX
        if self.rect.x <= 0 or self.rect.x >= largeur-self.rect.w :
            self.deltaX = - self.deltaX
            self.rect.x = self.rect.x

        self.rect.y += self.deltaY
        if self.rect.y <= 0 or self.rect.y >= hauteur-self.rect.h :
            self.deltaY = - self.deltaY
            self.rect.y = self.rect.y
