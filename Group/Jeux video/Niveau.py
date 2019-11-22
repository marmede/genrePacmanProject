import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee
class Tuile(ElementGraphiqueAnimee):
    def __init__(self,img,x=0,y=0):
        ElementGraphiqueAnimee.__init__(self,[img],x,y)
        self.image = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.plein = True

    def Update(self,x=0,y=0):
        if x != self.rect.x:
            self.rect.x = x
            self.alive = False
        if y != self.rect.y:
            self.rect.y = y
            self.alive = False
        self.rect = self.image.get_rect()

    def move(self,x=0,y=0,Niveau = []):
        self.rect.x += x
        self.rect.y += y
        Niveau.tab[int(self.rect.y/72)][int(self.rect.x/72)] = 0

    def isAlive(self):
        return self.alive;


class Niveau(ElementGraphiqueAnimee):
    def __init__(self,fichier,img,x=0,y=0):
        ElementGraphiqueAnimee.__init__(self,img,x,y)
        self.fichier = fichier
        self.images = img
        self.tab = []
        self.tab_mur = []

        self.test = False
        self.hauteur_tuile = self.images[0].get_height()
        self.largeur_tuile = self.images[0].get_width()

    def afficherLab(self,imMur,fenetre):
        rect = imMur[0].get_rect()
        self.mur = []
        for i in range(len(self.tab)):
            l = []
            for j in range(len(self.tab[i])):
                t = Tuile(imMur[self.tab[i][j]],j*rect.w,i*rect.h)
                fenetre.blit(t.image,(t.rect.x, t.rect.y))
                if(self.tab[i][j] == 0):
                    t.plein = False
                if(self.tab[i][j] == 1):
                    l.append(t)
            self.tab_mur.append(l)

    def PersoDirection(self,perso):
        if(perso.direction == "dos" or perso.last_direction == "dos_s" ):
                return 0,-1
        elif(perso.direction == "face" or perso.last_direction == "debout"):
                return 0,1
        elif(perso.direction == "droite" or perso.last_direction == "droite_s"):
                return 1,0
        elif(perso.direction == "gauche" or perso.last_direction == "gauche_s"):
                return -1,0

    def Update(self,perso):
        x,y = self.PersoDirection(perso)
        x_start = int((perso.rect.x)/32) 
        y_start = int((perso.rect.y)/32)
        nx = x_start + x
        ny = y_start + y
        if(self.tab[ny][nx] == 0):
            self.tab[ny][nx] = self.tab[y_start][x_start] 
            self.tab[y_start][x_start]  = 0

        if(self.tab[ny][nx] == 2):
            self.tab[y_start][x_start] = 0
            self.tab[ny][nx] = 0



        # if(self.tab[ny][nx] == 3) and self.tab[ny+(2*y)][nx+(2*x)] != 1 and self.tab[ny+y][nx+x] != 1:
            # # self.tab[ny+(2*y)][nx+(2*x)] = self.tab[ny+y][nx+x]
            # self.tab[ny+y][nx+x] = self.tab[ny][nx]
            # self.tab[y_start][x_start]  = 0
            # self.tab[ny+(2*y)][nx+(2*x)] = 0


    def createLab(self,hauteur, largeur, hautCase,largCase):

        hCase = int(hauteur/hautCase)+1
        lCase = int(largeur/largCase)+1

       	#Python ouvre le fichier
        with open(self.fichier, "r") as fichier:
            self.tab = []
            for ligne in fichier:
                l = []
                for i in ligne:
                    if i != '\n':
                            l.append(int(i))
                self.tab.append(l)
        return self.tab

    def editLab(self,hauteur,largeur,hautCase,largCase):
        hCase = int(hauteur/hautCase)+1
        lCase = int(largeur/largCase)+1
        # Nommer le fichier
        with open(nomfichier,"w") as fichier:
            for x in range(hCase):
                    for y in range(lCase):
                        fichier.write('0')
                    fichier.write('\n')




    # def Update(self,y,x):
    #   self.tab[y][x+1] = self.tab[y][x]
        # self.tab[y][x] = 0