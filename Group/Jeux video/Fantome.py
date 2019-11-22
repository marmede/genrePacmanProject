import pygame
from random import randint
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from JoueurAnimee import JoueurAnimee

class Fantome(JoueurAnimee):
        def __init__(self,img,x,y, mat =[], size = 72):
                ElementGraphiqueAnimee.__init__(self,img["debout"],x,y)
                self.deltaX = randint(-10,10)
                self.deltaY = randint(-10,10)
                self.rect.x = x
                self.rect.y = y
                self.collision = [False,False,False,False]
                self.image = img
                self.numimage = 0
                self.direction = "debout"


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
                # if (self.PixToCase(niveau,-12,0,1,0) == 1) or (self.PixToCase(niveau,-12,16,1,0) == 1):
                #         self.collision[2] = True
                # else:
                #         self.collision[2] = False

        def PixToCase(self,niveau,dx=0,dy=0,x=0,y=0):
                x_start = int((self.rect.x+dx)/32) + x
                y_start = int((self.rect.y+dy)/32) + y
                print(x_start)
                print(y_start) 
                return niveau.tab[y_start][x_start]

        def x(self):
                x_start = int((self.rect.x)/32)
                return x_start
        def y(self):
                y_start = int((self.rect.y)/32) 

        def Determiner_position(self):

                if self.collision[0]:
                        self.direction = "haut"
                        self.numimage += 1
                        self.deltaX = 0
                        self.deltaY = -10

                if self.collision[1]:
                        self.direction = "bas"
                        self.numimage += 1
                        self.deltaX = 0
                        self.deltaY = 10

                if self.collision[2]:
                        self.direction = "gauche"
                        self.numimage += 1
                        self.deltaX = -10
                        self.deltaY = 0

                if self.collision[3]:
                        self.direction = "droite"
                        self.numimage += 1
                        self.deltaX = 10
                        self.deltaY = 0
        

        def rebond(self,niveau):
                # self.VerifCollision(niveau)
                self.Determiner_position()
                if (self.collision[0] or self.collision[3]) and (self.rect.x >= 0 and self.rect.x <= 1184 - 16):
                        self.rect.x += self.deltaX
                if (self.collision[1] or self.collision[2]) and (self.rect.y >= 0 and self.rect.y <= 624):
                        self.rect.y += self.deltaY
                else:
                        self.deltaY = -self.deltaY
                                
        def Tombe(self,x,y):
                self.deltaY = randint(1,10)*-1
                self.rect.y -= self.deltaY
                if self.rect.y >= (y+50) :
                        self.alive = False

        def afficher(self, window) :
                if (self.fps % 1 )== 0:
                        self.numimage = (self.numimage)%len(self.image[self.direction])
                        window.blit(self.image[self.direction][self.numimage],self.rect,)