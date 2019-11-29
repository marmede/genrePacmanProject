import pygame
from random import randint
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from JoueurAnimee import JoueurAnimee

class Fantome(JoueurAnimee):
        def __init__(self,img,x,y, mat =[]):
                JoueurAnimee.__init__(self, img, x, y)
                self.deltaX = 0
                self.deltaY = 0
                self.rect.x = x
                self.rect.y = y
                self.vitesse = 2

        def Cooldown(self, niveau):
                tabrect = [self.rect_haut,self.rect_bas,self.rect_droite,self.rect_gauche]
                for rect in range(len(tabrect)):
                        if self.PixToCase(niveau) == 2:
                                self.alive = False

        def pathfinding(self, x, y):
                #à modifier avec du pathfinding
                dX, dY = 0, 0
                if self.rect.x - x > 0:
                        dX = -1
                if self.rect.x - x < 0:
                        dX = 1
                if self.rect.y - y > 0:
                        dY = -1
                if self.rect.y - y < 0:
                        dY = 1
                return dX, dY

        def VerifCollision(self,niveau):
                # print("HAUT")
                a = self.PixToCase(niveau,0,0,0,0)
                b = self.PixToCase(niveau,14,24,0,-1) 
                c = self.PixToCase(niveau,0,28,0,-1)
                d = self.PixToCase(niveau,14,0,0,1)
                e = self.PixToCase(niveau,24,16,-1,0)
                f = self.PixToCase(niveau,-12,0,1,0)
                g = self.PixToCase(niveau,-12,16,1,0)

                if (a == 1 or a == 3 or b == 1 or b == 3):
                    self.collision[0] = True
                else:
                    self.collision[0] = False

                # print("BAS")
                if (c == 1 or c == 3 or d == 1 or d == 3):
                    self.collision[1] = True
                else:
                    self.collision[1] = False

                # print("GAUCHE")
                if (a == 1 or a == 3 or e == 1 or e == 3):
                    self.collision[3] = True
                else:
                    self.collision[3] = False

                # print("DROITE")
                if (f == 1 or f == 3 or g == 1 or g == 3):
                    self.collision[2] = True
                else:
                    self.collision[2] = False

        def deplacer(self, niveau, fenetre, joueurX, joueurY):
                self.VerifCollision(niveau)
                self.Cooldown(niveau)
                self.deltaX, self.deltaY = self.pathfinding(joueurX, joueurY)

                self.rect_bas.x = self.rect.x
                self.rect_bas.y = self.rect.y + self.rect.h

                self.rect_droite.x = self.rect.x + self.rect.w + 3
                self.rect_droite.y = self.rect.y

                self.rect_gauche.x = self.rect.x - 3
                self.rect_gauche.y = self.rect.y

                self.rect_haut.x = self.rect.x
                self.rect_haut.y = self.rect.y

                largeur, hauteur = fenetre.get_size()
                if self.rect.x <= 0 or self.rect.x >= largeur-self.rect.w :
                        self.deltaX = - self.deltaX

                if self.rect.y <= 0 or self.rect.y >= hauteur-self.rect.h :
                        self.deltaY = - self.deltaY

                if self.rect.x <= 0:
                    self.collision[3] = True


                if self.rect.x >= 1184-16:
                    self.collision[2] = True

                if self.rect.y <= 0:
                    self.collision[0] = True

                if self.rect.y >= 624:
                    self.collision[1] = True

                if self.deltaY == -1:
                        self.direction = "haut"
                        self.last_direction = "haut"
                        self.numimage += 1
                        if not self.collision[0]:
                            self.move(0, -self.vitesse)             

                elif self.deltaY == 1:
                        self.direction = "bas"
                        self.last_direction = "bas"
                        self.numimage += 1
                        if not self.collision[1]:
                            self.move(0, self.vitesse)

                if self.deltaX == 1:
                        self.direction = "droite"
                        self.last_direction = "droite"
                        self.numimage += 1
                        if not self.collision[2]:
                            self.move(self.vitesse, 0)

                if self.deltaX == -1:
                        self.direction = "gauche"
                        self.last_direction = "gauche"
                        self.numimage += 1
                        if not self.collision[3]:
                            self.move(-self.vitesse, 0)
                                
                else:
                        self.direction = self.last_direction
                self.deltaX, self.deltaY = 0, 0
                #return self.joueurMort(joueurX, joueurY)