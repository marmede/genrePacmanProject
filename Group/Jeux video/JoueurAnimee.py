import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
from BalleTiree import BalleTiree

class JoueurAnimee(ElementGraphiqueAnimee):
        def __init__(self, img, x = 0, y = 0):
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
                self.last_direction = "debout"
                self.tire = []
                self.vitesse = 6
                self.collision = [False, False, False, False]
                self.rect_bas = pygame.Rect((self.rect.x,self.rect.y + self.rect.h),(30,1))
                self.rect_haut = pygame.Rect((self.rect.x,self.rect.y),(30,1))
                self.rect_droite = pygame.Rect((self.rect.x + self.rect.w + 3,self.rect.y),(1,30))
                self.rect_gauche = pygame.Rect((self.rect.x - 3,self.rect.y),(1,30))

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

        def Cooldown(self,niveau):
        		tabrect = [self.rect_haut,self.rect_bas,self.rect_droite,self.rect_gauche]
        		for rect in range(len(tabrect)):
        			if self.PixToCase(niveau) == 2:
        				self.collision[rect] = False
        				self.boost = 0.35
        			else:
        				self.boost = 1

        def PushBlock(self,niveau):
                if self.PixToCase(niveau) == 3:
                        niveau.Update(self)

        def move(self,dx=0,dy=0):
                self.rect.x += dx * self.boost
                self.rect.y += dy * self.boost

        def deplacer(self,niveau, touches, window):
                self.VerifCollision(niveau)
                self.Cooldown(niveau)
                self.PushBlock(niveau)

                self.rect_bas.x = self.rect.x
                self.rect_bas.y = self.rect.y + self.rect.h

                self.rect_droite.x = self.rect.x + self.rect.w + 3
                self.rect_droite.y = self.rect.y

                self.rect_gauche.x = self.rect.x - 3
                self.rect_gauche.y = self.rect.y

                self.rect_haut.x = self.rect.x
                self.rect_haut.y = self.rect.y

                largeur, hauteur = window.get_size()
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

        def Tire(self):
                if(self.last_direction == "dos_s"):
                        return 0,-10
                elif(self.last_direction == "debout"):
                        return 0,10
                elif(self.last_direction == "droite_s"):
                        return 10,0
                elif(self.last_direction == "gauche_s"):
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
