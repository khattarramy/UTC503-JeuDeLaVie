import pygame
#import random

class Cellule:
    def __init__(self, surface, grid_x,grid_y):
        self.vivant = False
        self.surface = surface
        self.grille_x = grid_x
        self.grille_y = grid_y
        self.image = pygame.Surface((20,20))
        self.rectangle = self.image.get_rect()
        self.voisins = []
        self.voisins_vivant = 0

    #--------------------------FONCTIONS POUR LA CELLULE----------------------------#
    
    def mettre_a_jour(self):
        self.rectangle.topleft = (self.grille_x*20,self.grille_y*20)
        for cellule in self.voisins:
            if cellule.vivant:
                self.voisins_vivant+=1

    def dessiner(self):
        if self.vivant:
            self.image.fill((255,255,255))
        else:
            self.image.fill((94,94,99))
            pygame.draw.rect(self.image,(0,0,0),(1,1,18,18))
        self.surface.blit(self.image,(self.grille_x*20,self.grille_y*20))

    def obtenir_voisins(self,grille):
        liste_voisins = [[1,1],[-1,-1],[-1,1],[1,-1],[0,-1],[0,1],[1,0],[-1,0]]
        for voisin in liste_voisins:
            voisin[0] += self.grille_x
            voisin[1] += self.grille_y
            if voisin[0] < 0:
                voisin[0] += 30
            if voisin[1] < 0:
                voisin[1] += 30
            if voisin[1] > 29:
                voisin[1] -= 30
            if voisin[0] > 29:
                voisin[0] -= 30
            try:
                self.voisins.append(grille[voisin[1]][voisin[0]])
            except:
                print(voisin)
    
    def vivre_voisins(self):
        count = 0
        for voisin in self.voisins:
            if voisin.vivant:
                count+=1
                
        self.voisins_vivant = count

        