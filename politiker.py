from spiller import Spiller

class Politiker:
    def __init__(self, navn):
        self.navn = navn
        self.pris = 20
        self.poengsum = 10
        self.saker = []
        
    def hent_poengsum(self):
        return self.poengsum

    def hent_pris(self):
        return self.pris

    def sak_sukess(self):
        self.poengsum += 50

    def sak_fiasko( self):
        self.poengsum -= 50


