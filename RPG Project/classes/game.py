import imp
import random
from .magic import spells
from .inventory import itens

class bcolors:
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    WHITE = "\033[97m"
    
class character:
    def __init__(self, hp, mp, atk, df, magic, item):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk = atk
        self.df = df
        self.magic = magic
        self.item = item
        self.actions = ["Attack","Magic","Itens","Exit"]

    def heal(self,healing):
        self.hp += healing
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def generate_damage(self):
        atkl = int(self.atk*0.95)
        atkh = int(self.atk*1.05)
        return random.randrange(atkl,atkh)
    
    def take_damage(self,dmg):
        self.hp -= (dmg-self.df)
        if self.hp<0:
            self.hp = 0
        return self.hp

    def reduce_mp(self,cost):
        self.mp -=cost

    def restore_mp(self,cost):
        self.mp +=cost
        if self.mp > self.max_mp:
            self.mp = self.max_mp

    def choose_action(self):
        i=1
        print(bcolors.GREEN + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print(str(i)+":",item)
            i+=1
    
    def choose_magic(self):
        i=1
        print(bcolors.BLUE + bcolors.BOLD + "SPELLS" + bcolors.ENDC)
        for spell in self.magic:
            print(str(i)+":",spell.name, bcolors.BLUE + bcolors.BOLD + "(Mana Cost:" + str(spell.cost) + ")" + bcolors.ENDC )
            i+=1
  
    def choose_item(self):
        i=1
        print(bcolors.YELLOW + bcolors.BOLD + "ITENS" + bcolors.ENDC)
        for item in self.item:
            print(str(i)+":" + bcolors.YELLOW + bcolors.BOLD + item.name + bcolors.ENDC )
            i+=1