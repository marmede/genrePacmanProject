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
        self.deplacement = False

    def afficher(self, window):
        self.numimage += 1
        if (self.fps % 30 )== 0:
            self.numimage = (self.numimage)%len(self.image[self.direction])
            window.blit(self.image[self.direction][self.numimage],self.rect)

    def pix2case(self, x, y):
        i = y/72
        j = x/72
        return i, j

    def veri2(self):
        ok = True
        icase, jcase = self.pix2case(self.rect.x, self.rect.y)
        if self.matrice[int(icase)+1][int(jcase)]!= "0":
            ok=False
        return ok

    def deplacer2(self):
        ok = self.veri2()
        if ok:
            self.direction = "droit"
            self.rect.x += self.vitesse*self.boost


    def verifCollision(self):

        if self.matrice[int((self.rect.x )/self.taille_tuile)][int(self.rect.y/self.taille_tuile)] != "0":#GAUCHE
            self.setLimite(((int((self.rect.y)/self.taille_tuile)+1)*72 - 44),0)
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

        if self.matrice[int((self.rect.y )/self.taille_tuile)-1][int(self.rect.x/self.taille_tuile)] != "0":#DROITE
            self.setLimite((int((self.rect.y)/self.taille_tuile)-1),3)
        else:
            self.limite[3] = 0


        if self.matrice[int((self.rect.x - 1 +self.rect.w)/self.taille_tuile)][int((self.rect.y+self.rect.h)/self.taille_tuile)-1] != "0":#DEBUGGER BAS
            self.setLimite((int(self.rect.y/self.taille_tuile))*72 + 74,1)
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

        alea = 0
        #ALORS ici en fait on va donner une direction de départ, de manière aléatoire
        if self.deplacement == False:
            alea = randint(0,1)
            if alea < 0.25:
                self.direction = "gauche"
            elif alea < 0.5:
                self.direction = "haut"
            elif alea < 0.75:
                self.direction = "droit"
            else:
                self.direction = "bas"
            self.deplacement = True

        #Ici on passe tous les cas où on aura une direction + collision
        if self.direction == "haut":
            if self.rect.y > 0:
                #self.last_direction = "dos_s"
                self.numimage += 1
                if self.rect.y > self.limite[1] or self.limite[1] == 0:
                    self.rect.y -= self.vitesse * self.boost
                else:
                    #Alors si y'a collision, on garde .y inchangé, par contre on va soit aller à gauche, soit à droite
                    #Avec l'aléatoire on va essayé de mettre un peu de diversité dans les déplacements
                    #et si y'a une collision a gauche et à droite, ben on repars dans le sens inverse, et c'est comme sa
                    #pour toute les directions. Donc en gros, les directions gèrent les déplacements
                    self.rect.y = self.rect.y
                    if randint(0,1) > 0.5:
                        if self.limite[3] < self.rect.x or self.limite[3] == 0:
                            self.direction = "gauche"
                        elif self.limite[0] > self.rect.x or self.limite[0] == 0:
                            self.direction = "droit"
                    elif self.limite[0] > self.rect.x or self.limite[0] == 0:
                        self.direction = "droit"
                    else:
                        self.direction = "bas"

        elif self.direction == "droit":
            if self.rect.x < largeur+self.rect.w:
                #self.last_direction = "droite_s"
                self.numimage += 1
                if self.limite[0] > self.rect.x or self.limite[0] == 0:
                    self.rect.x += self.vitesse * self.boost
                else:
                    self.rect.x = self.rect.x
                    if randint(0,1) > 0.5:
                        if self.rect.y < self.limite[2] or self.limite[2] == 0:
                            self.direction = "bas"
                        elif self.limite[1] < self.rect.x or self.limite[1] == 0:
                            self.direction = "haut"
                    elif self.limite[1] < self.rect.x or self.limite[1] == 0:
                            self.direction = "haut"
                    else:
                        self.direction = "gauche"      

        elif self.direction == "bas":
            if self.rect.y < hauteur-self.rect.h:
                #self.last_direction = "face"
                self.numimage += 1
                if self.rect.y < self.limite[2] or self.limite[2] == 0:
                    self.rect.y += self.vitesse * self.boost
                else:
                    self.rect.y = self.rect.y
                    if randint(0,1) > 0.5:
                        if self.rect.x < self.limite[0] or self.limite[0] == 0:
                            self.direction = "droit"
                        elif self.limite[3] < self.rect.x or self.limite[3] == 0:
                            self.direction = "gauche"
                    elif self.limite[3] < self.rect.x or self.limite[3] == 0:
                            self.direction = "gauche"
                    else:
                        self.direction = "haut"

        elif self.direction == "gauche":
            if self.rect.x > 0:
                self.last_direction = "gauche_s"
                self.numimage += 1
                if self.limite[3] < self.rect.x or self.limite[3] == 0:
                    self.rect.x -= self.vitesse * self.boost
                else:
                    self.limite[3] = 0
                    if randint(0,1) > 0.5:
                        if self.rect.y < self.limite[2] or self.limite[2] == 0:
                            self.direction = "bas"
                        elif self.limite[1] < self.rect.x or self.limite[1] == 0:
                            self.direction = "haut"
                    elif self.limite[1] < self.rect.x or self.limite[1] == 0:
                            self.direction = "haut"
                    else:
                        self.direction = "droit"
                
        else:
            self.direction = self.last_direction