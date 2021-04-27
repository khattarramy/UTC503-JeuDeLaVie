import pygame
import sys
from jeu_grille import *
from bouton import *

WIDTH, HEIGHT = 800, 800
BACKRGOUND = (94,94,99)
cadreparsecond = 60

def obtenir_evenements():
    global courant
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            courant = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            souris_pos = pygame.mouse.get_pos()
            if souris_sur_grille(souris_pos):
                click_cellule(souris_pos)
            else:
                for bouton in boutons:
                    bouton.click()

def mettre_a_jours():
    JeuGrille.mettre_a_jour()
    for bouton in boutons:
        bouton.mettre_a_jour(souris_pos, etat_jeu=etat)

def dessiner():
    fenetre.fill(BACKRGOUND) 
    dessiner_label()
    for bouton in boutons:
        bouton.dessiner()
    JeuGrille.dessiner()
    
def courant_mettre_a_jour():    
    if cadre_nombre%(cadreparsecond//10) == 0:
        JeuGrille.evaluer() 

def dessiner_label():
    myfont = pygame.font.SysFont("monospace", 20, True)
    label = myfont.render("Ramy Khattar - UTC 503 - Jeu de la vie", 1, (255,255,0))
    fenetre.blit(label, (100, 30))

def souris_sur_grille(pos):
    if pos[0]>100 and pos[0] < WIDTH-100:
        if pos[1]>180 and pos[1] < HEIGHT-20:
            return True
    return False

def click_cellule(pos):
    grille_pos = [pos[0]-100,pos[1]-180]
    grille_pos[0]=grille_pos[0]//20
    grille_pos[1]=grille_pos[1]//20
    if JeuGrille.grille[grille_pos[1]][grille_pos[0]].vivant:
        JeuGrille.grille[grille_pos[1]][grille_pos[0]].vivant = False
    else:
        JeuGrille.grille[grille_pos[1]][grille_pos[0]].vivant = True

def fabrique_boutons():
    boutons = []
    boutons.append(Bouton(fenetre,WIDTH//2-50,80,100,30,text='EXÉCUTER',bg_color=(28,11,51), hover_color=(48,131,81), bold_text=True, fonction=execute_jeu, etat='initial', font_name='monospace'))
    boutons.append(Bouton(fenetre,WIDTH//2-50,80,100,30,text='PAUSE',bg_color=(18,104,135), hover_color=(51,68,212), bold_text=True, fonction=pause_jeu, etat='encours', font_name='monospace'))
    boutons.append(Bouton(fenetre,WIDTH//5-50,80,160,30,text='RÉINITIALISER',bg_color=(117,14,14), hover_color=(217,54,54), bold_text=True, fonction=reset_grille, etat='paused', font_name='monospace'))
    boutons.append(Bouton(fenetre,WIDTH//1.25-50,80,120,30,text='CONTINUEZ',bg_color=(28,11,51), hover_color=(48,131,81), bold_text=True, fonction=execute_jeu, etat='paused', font_name='monospace'))
    return boutons

def execute_jeu():
    global etat
    etat = 'encours'

def pause_jeu():
    global etat
    etat = 'paused'

def reset_grille():
    global etat
    etat = 'initial'
    JeuGrille.reset_grille()

#-------------------------- MAIN FUNCTIONS ----------------------------#

pygame.init()
fenetre = pygame.display.set_mode((WIDTH,HEIGHT))
horloge = pygame.time.Clock()
JeuGrille = JeuGrille(fenetre, 100, 180)
boutons = fabrique_boutons()
etat = 'initial'
cadre_nombre = 0
courant = True

while courant:
    cadre_nombre += 1
    souris_pos = pygame.mouse.get_pos()
    obtenir_evenements()
    mettre_a_jours()  
    dessiner()  
    if etat == 'encours':
        courant_mettre_a_jour()  
    pygame.display.update()
    horloge.tick(cadreparsecond)

pygame.quit()
sys.exit()


    