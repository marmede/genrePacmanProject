import pygame
from random import randint
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from JoueurAnimee import JoueurAnimee

class Fantome(JoueurAnimee):
    def __init__(self,img,x,y, mat =[], size = 72):
        JoueurAnimee.__init__(self,img,x,y, mat, size)
        
        self.image = img
        self.numimage = 0
        self.direction = "debout"
        self.deltaX = randint(-5, 5)
        self.deltaY = randint(-5, 5)
        self.rect.x = x
        self.rect.y = y
        self;vitesse = 6
        self.deplacement = False

    def afficher(self, window):
        self.numimage += 1
        if (self.fps % 30 )== 0:
            self.numimage = (self.numimage)%len(self.image[self.direction])
            window.blit(self.image[self.direction][self.numimage],self.rect)

    def PixToCase(self,niveau,dx=0,dy=0,x=0,y=0):
            x_start = int((self.rect.x+dx)/32) + x
            y_start = int((self.rect.y+dy)/32) + y
            return niveau.tab[y_start][x_start]

    def VerifCollision(self,niveau):
            # print("HAUT")
            if (self.PixToCase(niveau,0,24,0,-1) == 1) or (self.PixToCase(niveau,14,24,0,-1) == 1):
                self.collision[0] = True
            else:
                self.collision[0] = False

            # print("BAS")
            if (self.PixToCase(niveau,0,28,0,-1) == 1) or (self.PixToCase(niveau,14,0,0,1) == 1):
                self.collision[1] = True
            else:
                self.collision[1] = False

            # print("GAUCHE")
            if (self.PixToCase(niveau,24,0,-1,0) == 1) or (self.PixToCase(niveau,24,16,-1,0) == 1):
                self.collision[3] = True
            else:
                self.collision[3] = False

            # print("DROITE")
            if (self.PixToCase(niveau,-12,0,1,0) == 1) or (self.PixToCase(niveau,-12,16,1,0) == 1):
                self.collision[2] = True
            else:
                self.collision[2] = False

    def deplacer(self, touches, window):
        self.verifCollision()
        if self.rect.x <= 0 or self.rect.x >= largeur-self.rect.w :
                self.deltaX = - self.deltaX

        if self.rect.y <= 0 or self.rect.y >= hauteur-self.rect.h :
                self.deltaY = - self.deltaY

        if touches[pygame.K_UP]:
                self.direction = "dos"
                self.last_direction = "dos_s"
                self.numimage += 1
                if not self.collision[0]:
                    self.move(0,-self.vitesse)                 

        elif touches[pygame.K_DOWN]:
                self.direction = "face"
                self.last_direction = "debout"
                self.numimage += 1
                if not self.collision[1]:
                    self.move(0,self.vitesse)

        elif touches[pygame.K_RIGHT]:
                self.direction = "droite"
                self.last_direction = "droite_s"
                self.numimage += 1
                if not self.collision[2]:
                    self.move(self.vitesse,0)

        elif touches[pygame.K_LEFT]:
                self.direction = "gauche"
                self.last_direction = "gauche_s"
                self.numimage += 1
                if not self.collision[3]:
                    self.move(-self.vitesse,0)
                        
        else:
                self.direction = self.last_direction


    def move(self,dx=0,dy=0):
            self.rect.x += dx * self.boost
            self.rect.y += dy * self.boost