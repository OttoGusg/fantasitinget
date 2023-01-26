

class Partier:
    def __init__(self, navn):
        self.navn = navn
        self.stemmeprosent = 0
        self.regjering = True or False 
        self.pris = 50
        self.poengsum = 50
        self.saker = []

    def regjering_poeng(self):
        if self.regjering == True:
            self.poengsum += 10 
        else: 
            return None 
        
    def sak_sukess(self):
        self.poengsum += 50

    def sak_fiasko( self):
        self.poengsum -= 50