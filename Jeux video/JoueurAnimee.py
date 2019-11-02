import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from BalleTiree import BalleTiree

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def pos(self):
        return (self.x,self.y)

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
                self.last_direction = "debout"
                self.tire = []
                self.vitesse = 12
                self.collision = [False, False, False, False] #[haut_droite|haut_gauche|bas_gauche|bas_droite]


        def Deplacer(self,touches,x,y,bloc):
                haut_g = Point((self.rect.x),(self.rect.y))
                haut_d = Point((self.rect.w + self.rect.x),(self.rect.y))
                bas_g = Point((self.rect.x),(self.rect.y + self.rect.h))
                bas_d = Point((self.rect.x + self.rect.w), (self.rect.y + self.rect.h))


                if touches [pygame.K_UP] :
                    self.direction = "dos"
                    self.last_direction = "dos_s"
                    self.numimage += 1
                    self.collision[0] = bloc.rect.collidepoint(haut_d.pos())
                    self.collision[1] = bloc.rect.collidepoint(haut_g.pos())
                    if  self.collision[0] == False and self.collision[1] == False:
                        self.rect.y -= self.vitesse * self.boost
                    else:
                        self.rect.y = self.rect.y

                elif touches [pygame.K_DOWN]:
                    self.direction = "face"
                    self.last_direction = "debout"
                    self.numimage += 1
                    self.collision[3] = bloc.rect.collidepoint(bas_d.pos())
                    self.collision[2] = bloc.rect.collidepoint(bas_g.pos())
                    if  self.collision[2] == False and self.collision[3] == False:
                        self.rect.y += self.vitesse * self.boost
                    else:
                        self.rect.y = self.rect.y

                elif touches [pygame.K_RIGHT]:
                        self.direction = "droite"
                        self.last_direction = "droite_s"
                        self.numimage += 1
                        self.collision[0] = bloc.rect.collidepoint(haut_d.pos())
                        self.collision[3] = bloc.rect.collidepoint(bas_d.pos())
                        if self.collision[0] == False and self.collision[3] == False:
                            self.rect.x += self.vitesse * self.boost
                        else :
                            self.rect.x = self.rect.x

                elif touches [pygame.K_LEFT]:
                        self.direction = "gauche"
                        self.last_direction = "gauche_s"
                        self.numimage += 1
                        self.collision[1] = bloc.rect.collidepoint(haut_g.pos())
                        self.collision[2] = bloc.rect.collidepoint(bas_g.pos())
                        if self.collision[1] == False and self.collision[2] == False :
                            self.rect.x -= self.vitesse * self.boost
                        else:
                            self.rect.x = self.rect.x
                else:
                        self.direction = self.last_direction

        def Tire(self):

            if(self.last_direction == "dos"):
                return 0,-10

            elif(self.last_direction == "face" or self.last_direction == "debout"):
                return 0,10

            elif(self.last_direction == "droite"):
                return 10,0

            elif(self.last_direction == "gauche"):
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
## fonction(bloc.collide(self),self.direction)
        def colliosion(self,rep,direction):
            if rep == True:
                if direction == "dos":
                    self.collision[0] = True
                else:
                    self.collision[0] = False