import keyboard
import os
import time
import random

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Character:
    def __init__(self, x, y, health, attack):
        self.x = int(x)
        self.y = int(y)
        self.health = int(health)
        self.attack = list(attack)

class Player(Character):
    def __init__(self, x, y, health, attack, weapon, level, xp, gold):
        super().__init__(x, y, health, attack)
        self.weapon = str(weapon)
        self.level = int(level)
        self.xp = int(xp)
        self.gold = int(gold)

class Enemy(Character):
    def __init__(self, x, y, health, attack):
        super().__init__(x, y, health, attack)

class Shop:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def print_alien_art():
    print("       _________")
    print("      /___   ___\\")
    print("     //@@@\ /@@@\\")
    print("     \\@@@/ \@@@//")
    print("      \\___  ___/")
    print("         | - |")
    print("          \\_/" + Colors.ENDC)

def print_shop_art():
    print(Colors.WARNING + "                ______________")
    print("    __,.,---'''''              '''''---..._")
    print(" ,-'             .....:::''::.:            '`-.")
    print("'           ...:::.....       '")
    print("            ''':::'''''       . ")
    print("            ''':::'''''       .               ,")
    print("|'-.._           ''''':::..::':          __,,-")
    print(" '-.._''`---.....______________.....---''__,,-")
    print("      ''`---.....______________.....---''" + Colors.ENDC)

def create_empty_lines():
    for _ in range(2):
        print("")

def enemy_prompt(exact_enemy):
    if exact_enemy.health <= 0:
        death_encounter(exact_enemy)
    else:
        answer = input(">: ").lower()
        if answer == "help":
            create_empty_lines()
            print("Attack | Run")
            time.sleep(4)
            enemy_encounter(exact_enemy)
        elif answer == "attack" and exact_enemy.health > 0:
            player_attack_value = random.randint(0, len(Player_1.attack) - 1)
            enemy_attack_value = random.randint(0, len(exact_enemy.attack) - 1)
            create_empty_lines()
            print("You have attacked the Alien...")
            create_empty_lines()
            exact_enemy.health -= Player_1.attack[player_attack_value]
            if player_attack_value == len(Player_1.attack) - 1:
                print(Colors.OKGREEN + "Critical hit on the alien!" + Colors.ENDC)
            print("(*) You did {0} damage to the alien!".format(Player_1.attack[player_attack_value]))
            print("")
            if enemy_attack_value == len(exact_enemy.attack) - 1:
                print(Colors.FAIL + "Critical hit on you!" + Colors.ENDC)
            Player_1.health -= exact_enemy.attack[enemy_attack_value]
            print("-[*]- The alien did {0} damage to you!".format(exact_enemy.attack[enemy_attack_value]))
            time.sleep(3)
            enemy_encounter(exact_enemy)
        elif answer == "run" and exact_enemy.health > 0:
            Decision = random.randint(0, 1)
            if Decision == 0:
                create_empty_lines()
                print("The Alien has caught you...")
                time.sleep(3)
                enemy_encounter(exact_enemy)
            elif Decision == 1:
                create_empty_lines()
                print("Got Away Safe and Sound...")
                create_empty_lines()
                print(Colors.OKGREEN + "Press W/A/S/D Keys to Move..." + Colors.ENDC)
        else:
            create_empty_lines()
            print("Unknown Command, Type help for help!")
            time.sleep(3)
            enemy_encounter(exact_enemy)

def death_prompt():
    answer = input(">: ").lower()
    if answer == "exit":
        create_empty_lines()
        print(Colors.OKGREEN + "Press W/A/S/D Keys to Move..." + Colors.ENDC)
    elif answer == "help":
        create_empty_lines()
        print("Exit | Tbag | Search")
        death_prompt()
    elif answer == "tbag":
        create_empty_lines()
        print("You Tbag the aliens dead corpse XD...")
        death_prompt()
    elif answer == "search":
        searched = False
        gold = random.randint(10, 15)
        if not searched:
            create_empty_lines()
            print("You found: " + Colors.WARNING + "{0}".format(gold) + Colors.ENDC + " Gold!")
            Player_1.gold += gold
            print("You now have {0} Gold!".format(Player_1.gold))
            searched = True
            death_prompt()
        else:
            print(Colors.FAIL + "You have already searched this Enemy..." + Colors.ENDC)
            death_prompt()
    else:
        create_empty_lines()
        print("Unknown Command, Type help for help!")
        death_prompt()

def enemy_encounter(exact_enemy):
    os.system('clear')
    print_alien_art()
    create_empty_lines()
    print("YOU HAVE ENCOUNTERED AN ENEMY!")
    print("")
    print("===============")
    print("Player Health: {0}".format(Player_1.health))
    print("Enemy Health: {0}".format(exact_enemy.health))
    print("===============")
    create_empty_lines()
    print("Type help for a list of actions...")
    create_empty_lines()
    enemy_prompt(exact_enemy)

def death_encounter(exact_enemy):
    exact_enemy.x = 99
    exact_enemy.y = 99
    del exact_enemy
    os.system('clear')
    print_alien_art()
    create_empty_lines()
    print("YOU HAVE KILLED AN ENEMY!")
    print("")
    print("Type help for a list of actions...")
    create_empty_lines()
    death_prompt()

def shop_prompt():
    create_empty_lines()
    answer = input(">: ").lower()
    if answer == "help":
        create_empty_lines()
        print("Buy Sword | Buy Mace | Buy Axe")
        time.sleep(4)
        shop_encounter()
    elif answer == "exit":
        print("Exiting...")
        create_empty_lines()
        print(Colors.OKGREEN + "Press W/A/S/D Keys to Move..." + Colors.ENDC)
    elif answer == "buy sword":
        if Player_1.gold < weapons[0][2]:
            print("You cannot afford the {0}...".format(weapons[0][0]))
        else:
            Player_1.gold -= weapons[0][2]
            Player_1.attack = weapons[0][1]
            Player_1.weapon = weapons[0][0]
            print("You have successfully Purchased the {0}...".format(weapons[0][0]))
        time.sleep(4)
        shop_encounter()
    elif answer == "buy mace":
        if Player_1.gold < weapons[1][2]:
            print("You cannot afford the {0}...".format(weapons[1][0]))
        else:
            Player_1.gold -= weapons[1][2]
            Player_1.attack = weapons[1][1]
            Player_1.weapon = weapons[1][0]
            print("You have successfully Purchased the {0}...".format(weapons[1][0]))
        time.sleep(4)
        shop_encounter()
    elif answer == "buy axe":
        if Player_1.gold < weapons[2][2]:
            print("You cannot afford the {0}...".format(weapons[2][0]))
        else:
            Player_1.gold -= weapons[2][2]
            Player_1.attack = weapons[2][1]
            Player_1.weapon = weapons[2][0]
            print("You have successfully Purchased the {0}...".format(weapons[2][0]))
        time.sleep(4)
        shop_encounter()    
    else:
        print("Unknown Command, Type help for help!")
        time.sleep(4)
        shop_encounter()

def shop_encounter():
    os.system('clear')
    print_shop_art()
    create_empty_lines()
    print("Gold: {0}".format(Player_1.gold))
    create_empty_lines()
    print("===============")
    for count, weapon in enumerate(weapons):
        print("{0} | Price: {1}".format(weapons[weapon][0], weapons[weapon][2]))
    print("===============")
    shop_prompt()

def title_screen():
    print(Colors.OKCYAN + "__  __    __  __   ____   __  _ "+ Colors.ENDC)
    print(Colors.OKCYAN + "\ \/ /   |  \/  | / () \ |  \| |"+ Colors.ENDC)
    print(Colors.OKCYAN + "/_/\_\   |_|\/|_|/__/\__\|_|\__|"+ Colors.ENDC)

def show_stats():
    print("===============")
    print(Colors.OKGREEN + "Health: " + Colors.ENDC + str(Player_1.health))
    print("Weapon: "+ Player_1.weapon)
    print(Colors.OKBLUE + "Level: " + Colors.ENDC + str(Player_1.level))
    print("XP: " + str(Player_1.xp))
    print(Colors.WARNING + "Gold: " + Colors.ENDC + str(Player_1.gold))
    print("===============")

def generate_board():
    Grid_Length = 30
    grid_line = ['-' for _ in range(Grid_Length)]
    holding_line = ''

    for count in range(len(grid_line)):
        if count == Player_1.y:
            grid_line[Player_1.x] = Colors.OKCYAN + 'x' + Colors.ENDC
        for enemy in enemy_list:
            if count == enemy.y:
                grid_line[enemy.x] = Colors.FAIL + 'E' + Colors.ENDC
        for shop in shop_list:
            if count == shop.y:
                grid_line[shop.x] = Colors.OKGREEN + 'S' + Colors.ENDC

        for index in range(len(grid_line)):
            holding_line += grid_line[index]
        print(holding_line)
        holding_line = ''

    create_empty_lines()
    show_stats()

def encounter_check():
    for enemy in enemy_list:
        if Player_1.x == enemy.x and Player_1.y == enemy.y:
            os.system('clear')
            enemy_encounter(enemy)
    for shop in shop_list:
        if Player_1.x == shop.x and Player_1.y == shop.y:
            os.system('clear')
            shop_encounter()

if __name__ == "__main__":
    Enemy_1 = Enemy(random.randint(3, 29), random.randint(3, 15), 60, [25, 22, 21, 30])
    Enemy_2 = Enemy(random.randint(3, 29), random.randint(3, 15), 60, [25, 22, 21, 30])
    Enemy_3 = Enemy(random.randint(3, 29), random.randint(3, 15), 60, [25, 22, 21, 30])
    Player_1 = Player(4, 4, 700, [25, 22, 21, 30], "None", 1, 0, 0)
    Shop_1 = Shop(1, 1)
    
    enemy_list = [Enemy_1, Enemy_2, Enemy_3]
    shop_list = [Shop_1]

    weapons = {0: ["Sword", [27, 24, 23, 32], 10], 1: ["Mace", [28, 25, 24, 33], 20], 2: ["Axe", [30, 27, 26, 35], 35]}
    os.system('clear')
    title_screen()
    time.sleep(2)
    os.system('clear')
    print(Colors.OKGREEN + "Press W/A/S/D Keys to Start..." + Colors.ENDC)

    while True:
        if keyboard.is_pressed('w'):
            for enemy in enemy_list:
                if 1 < enemy.y < 14:
                    enemy.y -= random.randint(-1, 1)
                elif enemy.y == 1:
                    enemy.y += 1
                elif enemy.y >= 14:
                    enemy.y -= 1
            os.system('clear')
            if Player_1.y > 0:
                Player_1.y -= 1
            generate_board()
            encounter_check()
            time.sleep(0.1)
        if keyboard.is_pressed('s'):
            for enemy in enemy_list:
                if 1 < enemy.y < 14:
                    enemy.y -= random.randint(-1, 1)
                elif enemy.y == 1:
                    enemy.y += 1
                elif enemy.y >= 14:
                    enemy.y -= 1
            os.system('clear')
            Player_1.y += 1
            generate_board()
            encounter_check()
            time.sleep(0.1)
        if keyboard.is_pressed('a'):
            for enemy in enemy_list:
                if 1 < enemy.x < 14:
                    enemy.x -= random.randint(-1, 1)
                elif enemy.x == 1:
                    enemy.x += 1
                elif enemy.x >= 14:
                    enemy.x -= 1
            os.system('clear')
            Player_1.x -= 1
            generate_board()
            encounter_check()
            time.sleep(0.1)
        if keyboard.is_pressed('d'):
            for enemy in enemy_list:
                if 1 < enemy.x < 14:
                    enemy.x -= random.randint(-1, 1)
                elif enemy.x == 1:
                    enemy.x += 1
                elif enemy.x >= 14:
                    enemy.x -= 1
            os.system('clear')
            Player_1.x += 1
            generate_board()
            encounter_check()
            time.sleep(0.1)