import random

class spells:
    def __init__(self,name,cost,efct,type):
        self.name = name
        self.cost = cost
        self.efct = efct
        self.type = type

    def generate_spell_dmg_efct(self):
        efct_low = int(self.efct * 0.95)
        efct_high = int(self.efct * 1.05)
        return random.randrange(efct_low,efct_high)

    def generate_spell_healing_efct(self):
        efct_low = int(self.efct * 0.95)
        efct_high = int(self.efct * 1.05)
        return random.randrange(efct_low,efct_high)











