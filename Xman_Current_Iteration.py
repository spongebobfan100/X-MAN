import keyboard
import os
import time
import random

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Player:
	def __init__(self, x, y, health, attack, weapon, level, xp, gold):			#Defines Player Object (What we control)
		self.x = int(x)
		self.y = int(y)
		self.health = int(health)
		self.attack = list(attack)
		self.weapon = str(weapon)
		self.level = int(level)
		self.xp = int(xp)
		self.gold = int(gold)

class Enemy:
	def __init__(self, x, y, health, attack):								#Defines Enemy Object
		self.x = int(x)
		self.y = int(y)
		self.health = int(health)
		self.attack = list(attack)

class Shop:
	def __init__(self, x, y):												#Defines the Shop Object
		self.x = int(x)
		self.y = int(y)

def alien_art(x):
	print(x + "       _________")
	print("      /___   ___\\")
	print("     //@@@\ /@@@\\")
	print("     \\@@@/ \@@@//")
	print("      \\___  ___/")
	print("         | - |")
	print("          \\_/" +colors.ENDC)

def shop_art():
	print(colors.WARNING + "                ______________")
	print("    __,.,---'''''              '''''---..._")
	print(" ,-'             .....:::''::.:            '`-.")
	print("'           ...:::.....       '")
	print("            ''':::'''''       . ")
	print("            ''':::'''''       .               ,")
	print("|'-.._           ''''':::..::':          __,,-")
	print(" '-.._''`---.....______________.....---''__,,-")
	print("      ''`---.....______________.....---''" + colors.ENDC)

def create_empty():															
	for count in range(2):
		print("")

def enemy_prompt(exact_enemy):
	if(exact_enemy.health <= 0):
		death_encounter(exact_enemy)
	else:
		answer = str(input(">: "))
		response = answer.lower()
		if(response == "help"):
			create_empty()
			print("Attack | Run")
			time.sleep(4)
			enemy_encounter(exact_enemy)
		elif(response == "attack" and exact_enemy.health > 0):
			player_attack_value = random.randint(0, len(Player_1.attack)-1)
			enemy_attack_value = random.randint(0, len(exact_enemy.attack)-1)
			create_empty()
			print("You have attacked the Alien...")
			create_empty()
			exact_enemy.health -= Player_1.attack[player_attack_value]
			if(player_attack_value == len(Player_1.attack)-1):
				print(colors.OKGREEN + "Critical hit on the alien!" + colors.ENDC)
			print("(*) You did {0} damage to the alien!".format(Player_1.attack[player_attack_value]))
			print("")
			if(enemy_attack_value == len(exact_enemy.attack)-1):
				print(colors.FAIL + "Critical hit on you!" + colors.ENDC)
			Player_1.health -= exact_enemy.attack[enemy_attack_value]
			print("-[*]- The alien did {0} damage to you!".format(exact_enemy.attack[enemy_attack_value]))
			time.sleep(3)
			enemy_encounter(exact_enemy)
		elif(response == "run" and exact_enemy.health > 0):
			Decision = random.randint(0, 1)
			if(Decision == 0):
				create_empty()
				print("The Alien has caught you...")
				time.sleep(3)
				enemy_encounter(exact_enemy)
			elif(Decision == 1):
				create_empty()
				print("Got Away Safe and Sound...")
				create_empty()
				print(colors.OKGREEN + "Press W/A/S/D Keys to Move..." + colors.ENDC)
		else:
			create_empty()
			print("Unknown Command, Type help for help!")
			time.sleep(3)
			enemy_encounter(exact_enemy)

def death_prompt():
	answer = str(input(">: "))
	response = answer.lower()
	if(response == "exit"):
		create_empty()
		print(colors.OKGREEN + "Press W/A/S/D Keys to Move..." + colors.ENDC)
	elif(response == "help"):
		create_empty()
		print("Exit | Tbag | Search")
		death_prompt()
	elif(response == "tbag"):
		create_empty()
		print("You Tbag the aliens dead corpse XD...")
		death_prompt()
	elif(response == "search"):
		searched = False
		gold = random.randint(10, 15)
		if(searched == False):
			create_empty()
			print("You found: "+colors.WARNING+"{0}".format(gold)+colors.ENDC+" Gold!")
			Player_1.gold += gold
			print("You now have {0} Gold!".format(Player_1.gold))
			searched = True
			death_prompt()
		else:
			print(colors.FAIL + "You have already searched this Enemy..." + colors.ENDC)
			death_prompt()
	else:
		create_empty()
		print("Unknown Command, Type help for help!")
		death_prompt()

def enemy_encounter(exact_enemy):
	os.system('clear')
	alien_art(colors.OKGREEN)
	create_empty()
	print("YOU HAVE ENCOUNTERED AN ENEMY!")
	print("")
	print("===============")
	print("Player Health: {0}".format(Player_1.health))
	print("Enemy Health: {0}".format(exact_enemy.health))
	print("===============")
	create_empty()
	print("Type help for a list of actions...")
	create_empty()
	enemy_prompt(exact_enemy)

def death_encounter(exact_enemy):
	exact_enemy.x = 99; exact_enemy.y = 99;
	del exact_enemy
	os.system('clear')
	alien_art(colors.FAIL)
	create_empty()
	print("YOU HAVE KILLED AN ENEMY!")
	print("")
	print("Type help for a list of actions...")
	create_empty()
	death_prompt()

def shop_prompt():
	create_empty()
	answer = str(input(">: "))
	response = answer.lower()
	if(response == "help"):
		create_empty()
		print("Buy Sword | Buy Mace | Buy Axe")
		time.sleep(4)
		shop_encounter()
	elif(response == "exit"):
		print("Exiting...")
		create_empty()
		print(colors.OKGREEN + "Press W/A/S/D Keys to Move..." + colors.ENDC)
	elif(response == "buy sword"):
		if(Player_1.gold < weapons[0][2]):
			print("You cannot afford the {0}...".format(weapons[0][0]))
		else:
			Player_1.gold -= weapons[0][2]
			Player_1.attack = weapons[0][1]
			Player_1.weapon = weapons[0][0]
			print("You have successfully Purchased the {0}...".format(weapons[0][0]))
		time.sleep(4)
		shop_encounter()
	elif(response == "buy mace"):
		if(Player_1.gold < weapons[1][2]):
			print("You cannot afford the {0}...".format(weapons[1][0]))
		else:
			Player_1.gold -= weapons[1][2]
			Player_1.attack = weapons[1][1]
			Player_1.weapon = weapons[1][0]
			print("You have successfully Purchased the {0}...".format(weapons[1][0]))
		time.sleep(4)
		shop_encounter()
	elif(response == "buy axe"):
		if(Player_1.gold < weapons[2][2]):
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
	shop_art()
	create_empty()
	print("Gold: {0}".format(Player_1.gold))
	create_empty()
	print("===============")
	for count in range(len(weapons)):
		print("{0} | Price: {1}".format(weapons[count][0], weapons[count][2]))
	print("===============")
	shop_prompt()

def title_screen():															#Creates The title screen
	print(colors.OKCYAN + "__  __    __  __   ____   __  _ "+ colors.ENDC)
	print(colors.OKCYAN + "\ \/ /   |  \/  | / () \ |  \| |"+ colors.ENDC)
	print(colors.OKCYAN + "/_/\_\   |_|\/|_|/__/\__\|_|\__|"+ colors.ENDC)

def show_stats():															#Prints player information for game
	print("===============")
	print(colors.OKGREEN + "Health: " + colors.ENDC + str(Player_1.health))
	print("Weapon: "+ Player_1.weapon)
	print(colors.OKBLUE + "Level: " + colors.ENDC + str(Player_1.level))
	print("XP: " + str(Player_1.xp))
	print(colors.WARNING + "Gold: " + colors.ENDC + str(Player_1.gold))
	print("===============")

def generate_Board():														#Real proud of this one, Optimized algorithm for board generation
	grid_line  = list()
	holding_line = ''
	Grid_Length = 30
	for count in range(Grid_Length):										#Appends inital holders for board
		grid_line.append('-')
	for count in range(int(len(grid_line)/2)):								#Finds y cord of player and appends the x poition to the board
		if(count == Player_1.y):
			grid_line.pop(Player_1.x)
			grid_line.insert(Player_1.x, colors.OKCYAN + 'x' + colors.ENDC)
		for tried in range(len(enemy_list)):								#Systamatically iterates through list of enemies and appends positions
			if(count == enemy_list[tried].y):
				grid_line.pop(enemy_list[tried].x)
				grid_line.insert(enemy_list[tried].x, colors.FAIL + 'E' + colors.ENDC)
		for shops in range(len(shop_list)):
			if(count == shop_list[shops].y):
				grid_line.pop(shop_list[shops].x)
				grid_line.insert(shop_list[shops].x, colors.OKGREEN + 'S' + colors.ENDC)
		for index in range(len(grid_line)):									#Makes Holding Line String Equal to the addition of the gird list
			holding_line += grid_line[index]
		print(holding_line)													#Outputs the current line 
		holding_line = ''
		grid_line = []
		for count in range(Grid_Length):									#Resets the Grid
			grid_line.append('-')
	create_empty()															
	show_stats()																										

def encounter_check():
	for count in range(len(enemy_list)):
		if(Player_1.x == enemy_list[count].x and Player_1.y == enemy_list[count].y):
			os.system('clear')
			enemy_encounter(enemy_list[count])
	for count in range(len(shop_list)):
		if(Player_1.x == shop_list[count].x and Player_1.y == shop_list[count].y):
			os.system('clear')
			shop_encounter()

if __name__ == "__main__":
	Enemy_1 = Enemy(3, 3, 60, [25, 22, 21, 30])
	Enemy_2 = Enemy(3, 1, 60, [25, 22, 21, 30])
	Enemy_3 = Enemy(4, 2, 60, [25, 22, 21, 30])
	Player_1 = Player(4, 4, 700, [25, 22, 21, 30], "None", 1, 0, 0)			
	Shop_1 = Shop(1, 1)
	
	enemy_list = [Enemy_1,Enemy_2,Enemy_3]
	shop_list = [Shop_1]													

	weapons = {0: ["Sword",[27, 24, 23, 32], 10], 1: ["Mace",[28, 25, 24, 33], 20], 2: ["Axe",[30, 27, 26, 35], 35]}
	os.system('clear')
	title_screen()
	time.sleep(2)
	os.system('clear')
	print(colors.OKGREEN + "Press W/A/S/D Keys to Start..." + colors.ENDC)
	while True:
		if(keyboard.is_pressed('w')):
				for iterate in range(len(enemy_list)):
					if(enemy_list[iterate].y > 0 and enemy_list[iterate].y < 30):
						enemy_list[iterate].y -= random.randint(-1,1)
					elif(enemy_list[iterate].y == 0):
						enemy_list[iterate].y += 1
					elif(enemy_list[iterate].y == 30):
						enemy_list[iterate].y -= 1
				os.system('clear')
				if(Player_1.y > 0):
					Player_1.y -= 1
				generate_Board()
				encounter_check()
				time.sleep(0.1)
		if(keyboard.is_pressed('s')):
				for iterate in range(len(enemy_list)):
					if(enemy_list[iterate].y > 0 and enemy_list[iterate].y < 30):
						enemy_list[iterate].y -= random.randint(-1,1)
					elif(enemy_list[iterate].y == 0):
						enemy_list[iterate].y += 1
					elif(enemy_list[iterate].y == 30):
						enemy_list[iterate].y -= 1											
				os.system('clear')
				Player_1.y += 1
				generate_Board()
				encounter_check()
				time.sleep(0.1)
		if(keyboard.is_pressed('a')):
				for iterate in range(len(enemy_list)):
					if(enemy_list[iterate].x > 0 and enemy_list[iterate].x < 30):
						enemy_list[iterate].x -= random.randint(-1,1)
					elif(enemy_list[iterate].x == 0):
						enemy_list[iterate].x += 1
					elif(enemy_list[iterate].x == 30):
						enemy_list[iterate].x -= 1
				os.system('clear')
				Player_1.x -= 1
				generate_Board()
				encounter_check()
				time.sleep(0.1)
		if(keyboard.is_pressed('d')):
				for iterate in range(len(enemy_list)):
					if(enemy_list[iterate].x > 0 and enemy_list[iterate].x < 30):
						enemy_list[iterate].x -= random.randint(-1,1)
					elif(enemy_list[iterate].x == 0):
						enemy_list[iterate].x += 1
					elif(enemy_list[iterate].x == 30):
						enemy_list[iterate].x -= 1
				os.system('clear')
				Player_1.x += 1
				generate_Board()
				encounter_check()
				time.sleep(0.1)
