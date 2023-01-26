class Spiller:
    def __init__(self, brukernavn):
        self.brukernavn = brukernavn
        self.stemmer = 100 
        self.politikere = []
        self.poengsum = 0

def kjøp_politiker(self, ny_politiker):
    self.politikere.append(ny_politiker)
    self.poengsum += ny_politiker.hent_poengsum()
    if ny_politiker.hent_pris() > self.stemmer:
        return f'Du har ikke nok stemmer til {ny_politiker}'
    else:
        self.stemmer -= ny_politiker.hent_pris()
        return f'Gratulerer du har kjøpt {ny_politiker}!!!'

def hent_politikere(self):
    return self._politikere

def selg_politiker(self):
    pass

def beregn_poengsum(self):
    return self.poengsum
        
