import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from BalleTiree import BalleTiree
from Niveau import Niveau

class JoueurAnimee(ElementGraphiqueAnimee):
        def __init__(self,img,x=0,y=0):
                ElementGraphiqueAnimee.__init__(self,img["debout"],x,y)
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

        def Deplacer(self,touches,x,y, niveau):
                if touches [pygame.K_UP]:
                        self.direction = "dos"
                        self.numimage += 1
                        self.rect.y -= 12 * self.boost
                        if self.rect.y <= -12 :

                        #il faut modifier sa parce que c'est utilisé uniquement dans le cas
                        #ou le perso se déplace de case en case, sauf que nous faudrait
                        #plutôt gérer les collisions j'pense
                                if niveau.structure[niveau.case_y-1][niveau.case_x] != "6":
                                        self.rect.y += 12 * self.boost
                collision = 0
                if touches [pygame.K_UP]:
                        self.direction = "dos"
                        self.numimage += 1
                        for img in niveau.tab:
                                if self.rect.colliderect(img.get_rect()) == False:
                                        collision = 0
                                else:
                                        collision = 1

                        if collision == 0:
                                self.rect.y -= 12 * self.boost
##                        if self.rect.y <= -12 :
##
##                        #il faut modifier sa parce que c'est utilisé uniquement dans le cas
##                        #ou le perso se déplace de case en case, sauf que nous faudrait
##                        #plutôt gérer les collisions j'pense
##                                self.rect.y += 12 * self.boost
                elif touches [pygame.K_DOWN]:
                        self.direction = "face"
                        self.numimage += 1
                        self.rect.y += 12 * self.boost
                        if self.rect.y >= y - 90 : #Bas de l'écran
                                if niveau.structure[niveau.case_y+1][niveau.case_x] != "6":
                                        self.rect.y -= 12 * self.boost
                elif touches [pygame.K_RIGHT]:
                        self.direction = "droite"
                        self.numimage += 1
                        self.rect.x += 12 * self.boost
                        if self.rect.x >= x - 80: #Côté droit
                                if niveau.structure[niveau.case_y][niveau.case_x+1] != "6":
                                        self.rect.x -= 12 * self.boost
                elif touches [pygame.K_LEFT]:
                        self.direction = "gauche"
                        self.numimage += 1
                        self.rect.x -= 12 * self.boost
                        if self.rect.x <= -20 :
                                if niveau.structure[niveau.case_y][niveau.case_x-1] != "6":
                                        self.rect.x += 12 * self.boost
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

        def shoot(self, touches, tire, images):
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP and event.key == pygame.K_s:
                        tire.append(BalleTiree(images["chomp"],self.setTire(self.Tire()),self.rect.x,self.rect.y))
                return tire, images
