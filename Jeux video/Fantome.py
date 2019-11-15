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

    def afficher(self, window):
        self.numimage += 1
        if (self.fps % 30 )== 0:
            self.numimage = (self.numimage)%len(self.image[self.direction])
            window.blit(self.image[self.direction][self.numimage],self.rect)

    def verifCollision(self):

        if self.matrice[int((self.rect.x )/self.taille_tuile)][int(self.rect.y/self.taille_tuile)] != "0":#GAUCHE
            self.setLimite(((int((self.rect.x )/self.taille_tuile)+1)*72 - 44),0)
        else:
            self.limite[0] = 0

        if self.matrice[int((self.rect.x )/self.taille_tuile)][int(self.rect.y/self.taille_tuile)-1] != "0":#HAUT
            self.setLimite((int(self.rect.y/self.taille_tuile))*72 + 4,1)
        else:
            self.limite[1] = 0

        if self.matrice[int((self.rect.x )/self.taille_tuile)][int(self.rect.y/self.taille_tuile)] != "0":#BAS
            self.setLimite((int(self.rect.y/self.taille_tuile)+1)*72 - 56 , 2)
        else:
            self.limite[2] = 0

        if self.matrice[int((self.rect.x )/self.taille_tuile)-1][int(self.rect.y/self.taille_tuile)] != "0":#DROITE
            self.setLimite((int((self.rect.x )/self.taille_tuile)-1)*72 + 74,3)
        else:
            self.limite[3] = 0


        if self.matrice[int((self.rect.x - 1 +self.rect.w)/self.taille_tuile)][int((self.rect.y+self.rect.h)/self.taille_tuile)-1] != "0":#DEBUGGER BAS
            self.setLimite((int(self.rect.y/self.taille_tuile))*72 + 4,1)
        else:
            self.limite[1] = 0

        if self.matrice[int((self.rect.x - 26 +self.rect.w)/self.taille_tuile)][int((self.rect.y+self.rect.h)/self.taille_tuile)-1] != "0":#DEBUGGER HAUT
            self.setLimite((int(self.rect.y/self.taille_tuile))*72 + 4,1)
        else:
            self.limite[1] = 0

        if self.matrice[int((self.rect.x +self.rect.w)/self.taille_tuile)-1][int((self.rect.y +self.rect.h)/self.taille_tuile)] != "0":#DEBUGGER GAUCHE
            self.setLimite((int((self.rect.x + 88 )/self.taille_tuile)-1)*72 + 4,3)
        else:
            self.limite[3] = 0

    def deplacer(self, touches, window):
        self.verifCollision()
        largeur, hauteur = window.get_size()
        if self.rect.x <= 0 or self.rect.x >= largeur-self.rect.w :
            self.deltaX = - self.deltaX

        if self.rect.y <= 0 or self.rect.y >= hauteur-self.rect.h :
            self.deltaY = - self.deltaY

        # alea = randint(0,1)

        # if alea < 0.:


        if touches[pygame.K_UP]:
            self.direction = "haut"
            #self.last_direction = "dos_s"
            self.numimage += 1
            if self.rect.y > self.limite[1] or self.limite[1] == 0:
                self.rect.y -= self.vitesse * self.boost
            else:
                self.rect.y = self.rect.y           

        elif self.rect.y >0:
            self.direction = "bas"
            #self.last_direction = "face"
            self.numimage += 1
            if self.rect.y < self.limite[2] or self.limite[2] == 0:
                self.rect.y += self.vitesse * self.boost
            else:
                self.rect.y = self.rect.y
            

        elif touches[pygame.K_RIGHT]:
            self.direction = "droit"
            self.last_direction = "droite_s"
            self.numimage += 1
            if self.limite[0] > self.rect.x or self.limite[0] == 0:
                self.rect.x += self.vitesse * self.boost
            else:
                self.rect.x = self.rect.x

        elif touches[pygame.K_LEFT]:
            self.direction = "gauche"
            self.last_direction = "gauche_s"
            self.numimage += 1
            if self.limite[3] < self.rect.x or self.limite[3] == 0:
                self.rect.x -= self.vitesse * self.boost
            else:
                self.limite[3] = 0
                
        else:
            self.direction = self.last_direction