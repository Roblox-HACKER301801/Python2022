######################
#imports
######################
from adventurelib import *

######################
#Define Bags
######################
Room.item = Bag()


######################
#Define Rooms
######################
print("""READ THIS: You are playing a game about china and the secrets that need to be uncovered, to win you need to reach the overseer office, \nand take the helicopter to win. If you see an \"Elevator Keycard\" you can shorten the name to just \"E K\" To search a room say \"search\", and press \"enter\" to do any command.\n If you don't have correct items and are stuck somewhere, use \"end it\".""")
mainoffice = Room("""Your inside a gloomy lobby to the tower that you work at. The smell of plastic fills your nose. There is also an elevator infront of you.""")
washrooms = Room("""You enter a bathroom stall. It smells awful and all there is to fill in the darkness are some Mao
zedong propaganda.""")
officeroom = Room("""A room filled with computers and desks.""")
administrationblock = Room("""A small room with a single desk and computer on it. Seems quite valuable
since it has warning sign on it. There is an elevator behind you.""")
#overseers office part:
ovreceptiondesk = Room("""You enter room which contains a computer and a seat. Nicely named \"Overseers reception\". There is an elevator behind you.""")
ovoffice = Room("""You enter the huge room, the only one with some sort of design, its got a casset player, and the most modern
pc setup, and a massive painting of Mao zedong on the wall. And a laptop on one of desks.""")
hallway = Room("""You enter a well-lit hallway with pictures of Mao-Zedong to both sides of your vision. Two locked double doors are infront of you, a key is required to access the office.\nWARNING: Once you enter the office you cannot go back due to the door system, so be sure that you have everything with you.""")
executiveoffice = Room("""You enter a more brighter room, within it are multiple smaller cubicals.""")
executivebathroom = Room("""You enter a stylish bathroom, A nice smooth smell of fresh air """)
helicopter = Room("""You open the door and enter the helipad, a black bullet proof helicopter is infront of you,
with the chinese insigmia on the side of it.""")
######################
#Define Connections
######################
mainoffice.east = washrooms
administrationblock.west = officeroom
ovreceptiondesk.east = executiveoffice
ovreceptiondesk.north = hallway
ovoffice.east = executivebathroom
ovoffice.west = helicopter
######################
#Define Items
######################
eleaccesskey = Item("elevator key","elevator keycard","elevator Key","elevator Keycard", "E K")
eleaccesskey.description = "The keycard with a bold text \"elevator\" on its side."

adminaccesskey = Item("admin keycard", "admin Keycard", "A K", "Administration Keycard")
adminaccesskey.description = "A keycard with a bold text \"admin\" on its side"

ovacesskey = Item("overseer keycard", "ov keycard", "overseer Keycard", "ov Key","O K")
ovacesskey.description = "A keycard with a bold text \"overseer\" on its side, with a text on its other side being \"ACCESS TO EVERYTHING\""

maobar = Item("mao bar","Mao Bar", "Chocolate", "chocolate", "choco", "Choco")
maobar.description = "A small bar of chocolate with Mao zedong's face on it. Ingrediants: LSD, Cocaine, Lean, p, weed, chocolate mix, flour, sugar, baking soda, vinahe, plastic, acid, more lean."

notepad = Item("Note", "note", "notepad", "Notepad")
notepad.description = "A notepad with most of the pages scribbled with unreadable chinese. One of it says \"EVACUATION: Due to multiple riots, all personnel are to evacuate via the main enterance.\""

helicopterkey = Item("Helicopter Key", "helicopter key", "chopper", "H K")
helicopterkey.description = "A metallic key with the keychain saying \"HELICOPTER\"."

pin = Item("pin","code","Pin","Code")
pin.description = "A small laminated card with the numbers \"50199\" on them... Looks useful."
######################
#Add Items to Bags
######################
washrooms.item.add(eleaccesskey)
executiveoffice.item.add(maobar)
mainoffice.item.add(notepad) 
administrationblock.item.add(adminaccesskey)
ovoffice.item.add(ovacesskey)
executiveoffice.item.add(pin)
executivebathroom.item.add(helicopterkey)
######################
#Define any variables
######################
current_room = mainoffice
inventory = Bag()
used_helicopterkey = False
used_pin = False
######################
#Binds (eg “@when(“look”))
######################

@when("have the mao")
def havemao():
	inventory.add(maobar)
	print("You feel like something is in your inventory.") 



@when("end it")
def endit():
	print("You take the cyanide pill that you've brang.")
	print("You foam out of your mouth and slowly close your eyes.")
	print("Cause of death: Suicide") 
	quit()



@when("washrooms")
@when("enter washrooms")  
def enter_washrooms():
	global current_room
	if current_room == mainoffice:
		print("You walk into the washrooms")
		current_room = washrooms
	else: 
		print("There isn't any washrooms around here.") 
	print(current_room)



@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You casually walk {direction}")
		print(current_room)
	else:
		print("You can't just go through walls.") 



@when("search")
def search():
	print(current_room)
	print(current_room.exits())
	if len(current_room.item) > 0:
		print("You see:")
		for item in current_room.item:
			print(item)



@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def get_item(item):
	if item in current_room.item:
		t = current_room.item.take(item)
		inventory.add(t)
		print(f"You picked up the {item}") 
	else:
		print(f"You can't see a {item}") 




@when("inventory")
def inventory_look():
	print("you have")
	for item in inventory:
		print(item)



@when("use ITEM")
def use(item):

	global current_room
	if inventory.find(item) and inventory.find(item)==adminaccesskey and current_room == hallway:
		print("You slide the admin key over the reader and a faint click is heard.")
		print("You open the door and enter the officeroom.") 
		current_room = ovoffice
		print(current_room) 
		used_adminaccesskey = True
	elif inventory.find(item) and inventory.find(item)==maobar:
		print("You tear the wrapper and see the chocolate, ingraved is mao zedongs face. You snap a piece off and slowly chew it.")
		print("It's disgusting but you fight through it, However, you start foaming in the mouth and slowly your breathing stops.")
		print("You lost! Cause of death: over-dose of multiple illegal substances.")
		quit()
	
	elif inventory.find(item) and inventory.find(item)==pin:
		print("You enter the pin into the laptop.")
		print("The computer beeps and opens a recent document which reads:")
		print("\"INCIDENT599\"\nThe Tiananmen Square protests, known as the June Fourth Incident (Chinese: 六四事件; pinyin: liùsì shìjiàn) in China, were student-led demonstrations held in Tiananmen Square, Beijing during 1989.\nIn what is known as the Tiananmen Square Massacre (Chinese: 天安门大屠杀; pinyin: Tiān'ānmén dà túshā),\ntroops armed with assault rifles and accompanied by tanks fired at the demonstrators and those trying to block the military's advance into Tiananmen Square.\nThe protests started on 15 April and were forcibly suppressed on 4 June when the government declared martial law and sent the People's Liberation Army to occupy parts of central Beijing.\nEstimates of the death toll vary from several hundred to several thousand, with thousands more wounded.\nThe popular national movement inspired by the Beijing protests is sometimes called the '89 Democracy Movement (Chinese: 八九民运; pinyin: Bājiǔ mínyùn) or the Tiananmen Square Incident (Chinese: 天安门事件; pinyin: Tiān'ānmén shìjiàn).\n\nESCAPE: You got your information, its time for you escape using the helicopter, you hear someone banging on the door, the shadows represent some sort of military. They dont look happy.")
		print("Note from Overseer: \"All personnel are to evacuate all buildings in case of an emergency protest from the Tianamen anti-communist party. Tianamen Square protests are to be renamed to the \'Picnic Incident\'.")
		used_pin = True
	
	elif inventory.find(item) and inventory.find(item)==helicopterkey and current_room == helicopter:
		print("You open the helicopter with the key and enter the cockpit, you flick some switches and start the motor.")
		print("The helicopter slowly rises and when you look back you see a team of chinese military run out of the office and attempt to shoot you down.")
		print("You fly off into the distance. You win!.")
		quit()
	
	elif item == "elevator":

		floor = input("Which floor? (0,1,2)\n>")
		if current_room == administrationblock and inventory.find("elevator key") and floor == "0":
			print("You flick the elevator key against the reader. It beeps twice and all the dails become green.")
			print("The level two dial glows green and the elevator moves, You step out when the doors open.")
			current_room = mainoffice
			print(current_room)
		elif current_room == administrationblock and inventory.find("elevator key") and floor == "2":
			print("You flick the elevator key against the reader. It beeps twice and all the dails become green.")
			print("The level two dial glows green and the elevator moves, You step out when the doors open.")
			current_room = ovreceptiondesk
			print(current_room)
		elif current_room == mainoffice and inventory.find("elevator key") and floor == "1":
			print("You flick the elevator key against the reader and select the first floor.")
			print("The elevator starts moving. It beeps twice and you step out when the doors open.")
			current_room = administrationblock
			print(current_room)
		elif current_room == mainoffice and inventory.find("elevator key") and floor == "2":
			print("You flick the elevator key against the reader. It beeps twice and all the dails become green.")
			print("The level two dial glows green and sends you up to the next level, You step out")
			current_room = ovreceptiondesk
			print(current_room)
		elif current_room == ovreceptiondesk and inventory.find("elevator key") and floor == "1":
			print("You flick the elevator key against the reader and select the first floor.")
			print("The elevator starts moving. It beeps twice and you step out when the doors open.")
			current_room = administrationblock
			print(current_room)
		elif current_room == ovreceptiondesk and inventory.find("elevator key") and floor == "0":
			print("You flick the elevator key against the reader and select the first floor.")
			print("The elevator starts moving. It beeps twice and you step out when the doors open.")
			current_room = mainoffice
			print(current_room)
		elif current_room not in [administrationblock,mainoffice,ovreceptiondesk]:
			print("There is no elevator here")
		else:
			print("Your either on that floor, or the floor you've selected isn't real or you don't have the correct card in your inventory (Check \"inventory\").")
	
	else:

		print("You can't use that here")


@when("look at ITEM")
def look_at_item(item):
	if item in inventory:
		print(inventory.find(item).description)
######################
#Main Function
######################






#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE 
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
#start the main loop

if __name__ == '__main__':
	main()