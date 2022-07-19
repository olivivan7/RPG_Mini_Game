#Importing Libraries
import math

#Importing Classes
from classes.game import character, bcolors
from classes.magic import spells
from classes.inventory import itens


#Initializing Spells
fireball = spells("Fireball",10,160,"Fire")
lighting = spells("Lighting",15,180,"Thunder")
blizzard = spells("Blizzard",12,170,"Ice")
meteor = spells("Meteor",18,300,"Fire")
heal = spells("Heal",10,100,"Healing")

player_spells = [fireball,lighting,blizzard,meteor,heal]
enemy_spells = []


#Initializing Itens
potion = itens("Healing Potion","Potion","Heals 70 HP",70,0,0)
hipotion = itens("Hi-Potion","Potion","Heals 140 HP",140,0,0)
mana_potion = itens("Mana Potion","Potion","Recovers 30 MP",0,30,0)
hi_mana_potion = itens("Hi-Mana Potion","Potion","Recovers 80 MP",0,80,0) 
elixer = itens("Elixir", "Potion", "Restores 70 HP and 40MP",70,40,0)
blessing_water = itens("Blessing Water","Potion","Restores full HP and MP and Freezes the Enemy for one turn.",500, 60, 0)
fire_arrow = itens("Fire Arrow","Arrow","Deals 50 Fire Damage",0,0,50)
ice_arrow =itens("Ice Arrow","Arrow","Deals 30 Ice Damage and Freezes the Enemy for one turn.",0,0,30)
thunder_arrow = itens("Thunder Arrow","Arrow","Deals 40 Thunder Damage",0,0,40)

player_itens = [potion,mana_potion,blessing_water,fire_arrow,ice_arrow]
enemy_itens = []


#Initializing Characters
player = character(500,60,100,20,player_spells,player_itens)
enemy = character(1000,65,35,25,enemy_spells,enemy_itens)


#Starting the program
running = True
i=0
freeze_time = 0

print(bcolors.RED + bcolors.BOLD + "\nAN ENEMY HAS ATTACKED!" + bcolors.ENDC)

print("=========================================================")
print("Player HP:", bcolors.GREEN + bcolors.BOLD + str(player.hp) + "/" + str(player.max_hp) + bcolors.ENDC)
print("Player MP:", bcolors.BLUE + bcolors.BOLD + str(player.mp) + "/" + str(player.max_mp) + bcolors.ENDC)
print("Enemy HP:", bcolors.RED + bcolors.BOLD + str(enemy.hp) + "/" + str(enemy.max_hp) + bcolors.ENDC)
print("=========================================================")
            

while running:
    print("")
    player.choose_action()
    choice = int(input("Choose action:"))-1
    print("")

    #Direct Attack
    if choice == 0:
        playerdmg = player.generate_damage()
        enemy.take_damage(playerdmg)
        print(bcolors.GREEN + bcolors.BOLD + "Your attack dealt", playerdmg, "points of damage!" + bcolors.ENDC)

    #Choosing Spells
    elif choice == 1:
        player.choose_magic()
        spell_choice = int(input("Choose Spell:"))-1
        
        spell = player.magic[spell_choice]

        #Mana Validation
        current_mp = player.mp
        if spell.cost > current_mp:
            print(bcolors.RED + bcolors.BOLD + "\nNOT ENOUGH MANA POINTS!\n" + bcolors.ENDC)

            print("=========================================================")
            print("Player HP:", bcolors.GREEN + bcolors.BOLD + str(player.hp) + "/" + str(player.max_hp) + bcolors.ENDC)
            print("Player MP:", bcolors.BLUE + bcolors.BOLD + str(player.mp) + "/" + str(player.max_mp) + bcolors.ENDC)
            print("Enemy HP:", bcolors.RED + bcolors.BOLD + str(enemy.hp) + "/" + str(enemy.max_hp) + bcolors.ENDC)
            print("=========================================================")
            continue

        player.reduce_mp(spell.cost)

        #Generating Spell Effect
        if spell_choice == 4:
            healing_points = spell.generate_spell_healing_efct()
            player.heal(healing_points)
            print(bcolors.GREEN + bcolors.BOLD + "\n" + spell.name + " healed", str(healing_points), "points of health!" + bcolors.ENDC)
            print(bcolors.YELLOW + bcolors.BOLD + "[" + spell.type + "]\n" + bcolors.ENDC)
        elif spell_choice == -1:
            continue
        else:
            spell_dmg = spell.generate_spell_dmg_efct()
            enemy.take_damage(spell_dmg)
            print(bcolors.GREEN + bcolors.BOLD + "\n" + spell.name + " dealt", str(spell_dmg), "points of damage!" + bcolors.ENDC)
            print(bcolors.YELLOW + bcolors.BOLD + "[" + spell.type + "]\n" + bcolors.ENDC)

    #Choosing Itens
    elif choice == 2:
        player.choose_item()
        item_choice = int(input("Choose your Item:"))-1
        
        item = player.item[item_choice]
        
        #Generating Item Effect
        #Healing Potion
        if item_choice == 0:
            player.heal(item.hp)
            print(bcolors.GREEN + bcolors.BOLD + "\n" + item.name + " healed", str(item.hp), "points of health!" + bcolors.ENDC)
            print(bcolors.YELLOW + bcolors.BOLD + "[" + item.type + "]\n" + bcolors.ENDC)
        
        #Mana Potion
        elif item_choice == 1:
            player.restore_mp(item.mp)
            print(bcolors.BLUE + bcolors.BOLD + "\n" + item.name + " restored", str(item.mp), "points of mana!" + bcolors.ENDC)
            print(bcolors.YELLOW + bcolors.BOLD + "[" + item.type + "]\n" + bcolors.ENDC)
        
        #Bleessing Water
        elif item_choice == 2:
            player.heal(item.hp)
            player.restore_mp(item.mp)
            freeze_time += 1
            print(bcolors.GREEN + bcolors.BOLD + "\n" + item.name + " healed", str(item.hp), "points of health!" + bcolors.ENDC)
            print(bcolors.BLUE + bcolors.BOLD + item.name + " restored", str(item.mp), "points of mana!" + bcolors.ENDC)
            print(bcolors.YELLOW + bcolors.BOLD + "[" + item.type + "]\n" + bcolors.ENDC)

        #Fire Arrow    
        elif item_choice == 3:
            enemy.take_damage(item.dmg)
            print(bcolors.RED + bcolors.BOLD + "\n" + item.name + " dealt", str(item.dmg), "points of damage!" + bcolors.ENDC)
            print(bcolors.YELLOW + bcolors.BOLD + "[" + item.type + "]\n" + bcolors.ENDC)

        #Ice Arrow
        elif item_choice == 4:
            enemy.take_damage(item.dmg)
            freeze_time += 1
            print(bcolors.BLUE + bcolors.BOLD + "\n" + item.name + " dealt", str(item.dmg), "points of damage!" + bcolors.ENDC)
            print(bcolors.YELLOW + bcolors.BOLD + "[" + item.type + "]\n" + bcolors.ENDC)
        else:
            continue
    
    #Exit choice
    else:
        break

    
    #Enemy turn
    if freeze_time == 0:
        enemydmg = enemy.generate_damage()
        player.take_damage(enemydmg)
        print(bcolors.RED + bcolors.BOLD + "Enemy attack dealt",enemydmg,"points of damage!\n" + bcolors.ENDC)
    else:
        freeze_time -= 1

    #Combat Results
    print("=========================================================")
    print("Player HP:", bcolors.GREEN + bcolors.BOLD + str(player.hp) + "/" + str(player.max_hp) + bcolors.ENDC)
    print("Player MP:", bcolors.BLUE + bcolors.BOLD + str(player.mp) + "/" + str(player.max_mp) + bcolors.ENDC)
    print("Enemy HP:", bcolors.RED + bcolors.BOLD + str(enemy.hp) + "/" + str(enemy.max_hp) + bcolors.ENDC)
    print("=========================================================")

    #Final Results
    if enemy.hp == 0:
        print(bcolors.GREEN + bcolors.BOLD + "YOU WON THE BATTLE!\n" + bcolors.ENDC)
        running = False
    elif player.hp == 0:
        print(bcolors.RED + bcolors.BOLD + "YOU LOST THE BATTLE!\n" + bcolors.ENDC)
        running = False
    




















