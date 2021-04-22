import  pygame
vec = pygame.math.Vector2

class Bouton:
    def __init__(self,surface,x,y,width,height,etat='',id='',fonction=0,bg_color=(255,255,255),hover_color=(255,255,255), border=True,border_width=2, border_color=(0,0,0), text=None, text_size=16,text_color=(255,255,255),bold_text=False,hovered=False, font_name='monospace'):
        self.type = 'Bouton'
        self.surface = surface
        self.x = x
        self.y = y
        self.pos = vec (x,y)
        self.width = width
        self.height = height
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.etat = etat
        self.id = id
        self.bg_color = bg_color
        self.border_color = border_color
        self.border = border
        self.border_width = border_width
        self.hover_color = hover_color
        self.hovered = False
        self.fonction = fonction
        self.text = text
        self.bold_text = bold_text
        self.text_color = text_color
        self.text_size = text_size
        self.font_name = font_name
        self.showing = True

    #--------------------------FONCTIONS POUR LES BOUTONS----------------------------#

    def mettre_a_jour(self,pos,game_state=''):
        if self.souris_survol(pos):            
            self.hovered = True
        else:
            self.hovered = False
        if self.etat == '' or game_state == '':
            self.showing = True
        else:
            if self.etat == game_state:
                self.showing = True
            else:
                self.showing = False
    
    def dessiner(self):
        if self.showing:
            if self.border:
                self.image.fill(self.border_color)
                if self.hovered:
                    pygame.draw.rect(self.image,self.hover_color,(self.border_width,self.border_width,self.width-(self.border_width*2),self.height-(self.border_width*2)))
                else:
                    pygame.draw.rect(self.image,self.bg_color,(self.border_width,self.border_width,self.width-(self.border_width*2),self.height-(self.border_width*2)))
            else:
                self.image.fill(self.bg_color)
            if len(self.text)>0:
                self.afficher()
            self.surface.blit(self.image,self.pos)

    def click(self):
        if self.fonction != 0 and self.hovered:
            self.fonction()
    
    def afficher(self):
        font = pygame.font.SysFont(self.font_name,self.text_size,bold=self.bold_text)
        text = font.render(self.text,False,self.text_color)
        size = text.get_size()
        x, y = self.width//2-(size[0]//2),self.height//2-(size[1]//2)
        pos = vec(x,y)
        self.image.blit(text,pos)

    def souris_survol(self,pos):
        if self.showing:
            if pos[0] > self.pos[0] and pos[0] < self.pos[0]+self.width:
                if pos[1] > self.pos[1] and pos[1] < self.pos[1]+self.height:
                    return True
            else:
                return False
        else: 
            return False   
        

