import pygame

class Niveau:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        #on va créer une liste pour une chaque ligne, et une liste avec toute
        #les lignes
        
        #Python ouvre le fichier
        with open(self.fichier, "r") as fichier:
            structure_niveau = []

            #On parcourt les lignes du fichier
            for ligne in fichier:
                ligne_niveau = []
                #Pour chaque occurence dans le fichier
                for sprite in ligne:
                    if sprite != '\n':
                        #on ajoute l'occurence dans la liste de la ligne
                        ligne_niveau.append(sprite)
                #on ajoute la ligne dans la structure
                structure_niveau.append(ligne_niveau)

            self.structure = structure_niveau

    def afficher(self, fenetre, mur):
        #on va parcourir la liste
        num_ligne = 0
        for ligne in self.structure:
            #on va parcourir les lignes
            num_case = 0
            for sprite in ligne:
                #position en pixel (96 = taille du mur, pour le test)
                x = num_case * 96
                y = num_ligne * 96

                if sprite == "6":
                    fenetre.blit(mur, (x,y))

                num_case += 1
            num_ligne += 1
                
