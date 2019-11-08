import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee

class Niveau(ElementGraphique):
    def __init__(self,fichier,img,x=0,y=0):
        ElementGraphique.__init__(self,img,x,y)
        self.fichier = fichier
        self.tab = []
        self.test = False

    def afficherLab(self,lab,imMur,fenetre):
	    rect = imMur.get_rect()

	    for i in range(len(lab)):
	        for j in range(len(lab[i])):
	            if lab[i][j]==1:
	                fenetre.blit(imMur,(j*rect.w, i*rect.h))

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
        #print(tab)
        return self.tab

    def editLab(self,hauteur,largeur,hautCase,largCase):
        hCase = int(hauteur/hautCase)+1
        lCase = int(largeur/largCase)+1

        with open(self.fichier,"w") as fichier:
            for x in range(hCase):
                    for y in range(lCase):
                        fichier.write('0')
                    fichier.write('\n')
