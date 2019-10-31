import pygame
from ElementGraphiqueAnimee import ElementGraphiqueAnimee

class Niveau(ElementGraphiqueAnimee):
    def __init__(self,fichier,img,x=0,y=0):
        ElementGraphiqueAnimee.__init__(self,img,x,y)
        self.fichier = fichier
        self.tab = []

    def afficherLab(self,lab,imMur,fenetre):
	    rect = imMur[0].get_rect()

	    for i in range(len(lab)):
	        for j in range(len(lab[i])):
	            if lab[i][j]==1:
	                fenetre.blit(imMur[0],(j*rect.w, i*rect.h))

    def createLab(self,hauteur, largeur, hautCase,largCase):
        hCase = int(hauteur/hautCase)+1
        lCase = int(largeur/largCase)+1

       	#Python ouvre le fichier
        with open(self.fichier, "r") as fichier:
            tab = []
            for ligne in fichier:
                l = []
                for i in ligne:
                    if i != '\n':
                            l.append(int(i))
                tab.append(l)
        #print(tab)
        return tab