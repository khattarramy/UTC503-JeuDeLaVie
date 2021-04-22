import pygame
import copy
import itertools
from cellule import *
vec = pygame.math.Vector2

class JeuGrille:
    def __init__(self,ecran,x,y):
        self.ecran = ecran
        self.pos = vec(x,y)
        self.width, self.height = 600, 600
        self.image = pygame.Surface((self.width,self.height))
        self.rectangle = self.image.get_rect()
        self.lignes = 30
        self.colonnes = 30
        self.grille = [[Cellule(self.image,x,y) for x in range(self.colonnes)] for y in range(self.lignes)]
        for ligne in self.grille:
            for cellule in ligne:
                cellule.obtenir_voisins(self.grille)
        pygame.display.set_caption("Ramy Khattar - UTC 503 - Jeu de la vie","")
    
    
    #--------------------------FONCTIONS POUR LA GRILLE----------------------------#

    def mettre_a_jour(self):
        self.rectangle.topleft =  self.pos
        for ligne in self.grille:
            for cellule in ligne:
                cellule.mettre_a_jour()

    def dessiner(self):
        self.image.fill((0,0,0))
        for ligne in self.grille:
            for cellule in ligne:
                cellule.dessiner()
        self.ecran.blit(self.image,(self.pos.x, self.pos.y))

    def reset_grille(self):
        self.grille = [[Cellule(self.image,x,y) for x in range(self.colonnes)] for y in range(self.lignes)]
        for ligne in self.grille:
            for cellule in ligne:
                cellule.obtenir_voisins(self.grille)

    def evaluer(self):
        nouveau_grille = copy.copy(self.grille)
        for ligne in self.grille:
            for cellule in ligne:
                cellule.vivre_voisins()
        for yidx, ligne in enumerate(self.grille):
            for xidx, cellule in enumerate(ligne):
                if cellule.vivant:
                    if cellule.voisins_vivant == 2 or cellule.voisins_vivant == 3:
                        nouveau_grille[yidx][xidx].vivant = True
                    if cellule.voisins_vivant < 2:
                        nouveau_grille[yidx][xidx].vivant = False
                    if cellule.voisins_vivant > 3:
                        nouveau_grille[yidx][xidx].vivant = False
                else:
                    if cellule.voisins_vivant == 3:
                        nouveau_grille[yidx][xidx].vivant = True



                