import pygame
import random
import math
from BalleAnimee import BalleAnimee

class BalleTiree(BalleAnimee):
        def __init__(self,img,delta = [],px=0,py=0):
                BalleAnimee.__init__(self,img)
                self.img = img
                self.alive = True
                self.delta = delta
                self.rect.y = py+self.delta[1]
                self.rect.x = px+self.delta[0]
                self.tps = 0
                self.timer = True

        def existe(self):
                if self.rect.y <= 0 or self.rect.y >= 510 or self.rect.x <= -10 or self.rect.x >= 650 :
                        return False
                return True

        def Tire(self,x,y):
                self.rect.x += self.delta[0]
                if self.rect.x <= -100 or self.rect.x >= x+50 :
                        self.alive = False

                self.rect.y += self.delta[1]
                if self.rect.y <= -100 or self.rect.y >= y+50 :
                        self.alive = False
