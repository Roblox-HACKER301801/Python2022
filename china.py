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
print("""READ THIS: You are playing a game about china and the secrets that need to be uncovered, to win you need to reach the overseer office,
	and take the helicopter to win. If you see an \"Elevator Keycard\" you can shorten the name to just \"E K\" To search a room say \"search\", and press \"enter\" to do any command.""")
mainoffice = Room("""Your inside a gloomy lobby to the tower that you work at. The smell of plastic fills your nose. """)
elevatortwo = Room("""You've entered the elevator, all you see is a greasy set of dails and a Mao Zedong poster, The access reader glows red. You need a keycard.""")
elevatorthree = Room("""You enter another elevator to the floor above yours. The faint radio filled with chinese propaganda fills the room. You need an executive elevator key to use the elevator.""")

washrooms = Room("""You enter a bathroom stall. It smells awful and all there is to fill in the darkness are some Mao
zedong propaganda.""")
officeroom = Room("""A room filled with computers and desks. Looks like some sort of executive elevator keycard on one of the desks.""")
administrationblock = Room("""A small room with a single desk and computer on it. Seems quite valuable
since it has warning sign on it.""")
#overseers office part:
ovreceptiondesk = Room("""You enter  room which contains a computer and a seat. Nicely named \"Overseers reception\".""")
ovoffice = Room("""You enter the huge room, the only one with some sort of design, its got a casset player, and the most modern
pc setup, and a massive painting of Mao zedong on the wall.""")
hallway = Room("""You enter a well-lit hallway with pictures of Mao-Zedong to both sides of your vision. Two double doors are at the end of the hallway.""")
executiveoffice = Room("""You enter a more brighter room, within it are multiple smaller cubicals.""")
executivebathroom = Room("""You enter a stylish bathroom, A nice smooth smell of fresh air """)
helicopter = Room("""You open the door and enter the helipad, a black bullet proof helicopter is infront of you,
with the chinese insigmia on the side of it.""")
######################
#Define Connections
######################
mainoffice.north = elevatortwo
mainoffice.east = washrooms
"""
elevatortwo.north = administrationblock
"""
administrationblock.west = officeroom
administrationblock.north = elevatorthree

"""
elevatorthree.north = ovreceptiondesk
"""
ovreceptiondesk.east = executiveoffice
ovreceptiondesk.north = hallway
"""
hallway.north = ovoffice
"""
ovoffice.east = executivebathroom
ovoffice.west = helicopter
######################
#Define Items
######################
eleaccesskey = Item("elevator key","elevator keycard","elevator Key","elevator Keycard", "E K")
eleaccesskey.description = "The keycard with a bold text \"elevator\" on its side."

adminaccesskey = Item("admin keycard", "admin Keycard", "A K", "Administration Keycard")
adminaccesskey.description = "A keycard with a bold text \"admin\" on its side"

ovacesskey = Item("overseer keycard", "ov keycard", "overseer Keycard", "ov Key")
ovacesskey.description = "A keycard with a bold text \"overseer\" on its side, with a text on its other side being \"ACCESS TO EVERYTHING\""

maobar = Item("mao bar","Mao Bar", "Chocolate", "chocolate", "choco", "Choco")
maobar.description = "A small bar of chocolate with Mao zedong's face on it. Ingrediants: LSD, Cocaine, Lean, p, weed, chocolate mix, flour, sugar, baking soda, vinahe, plastic, acid, more lean."

maopro = Item("propaganda", "poster")
maopro.description = "A poster with Mao zedong's massive face glearing back at you. Under the face it says \"For china!\""

notepad = Item("Note", "note", "notepad", "Notepad")
notepad.description = "A notepad with most of the pages scribbled with unreadable chinese. One of it says \"EVACUATION: Due to multiple riots, all personnel are to evacuate via the main enterance.\""

exelevatorkey = Item("Executive Elevator Key", "executive elevator key", "Executive Keycard", "Executive Keycard", "E E K")
exelevatorkey.description = "A black keycard with the insigmia of the CCP on one side, and the words \"EXECUTIVE ELEVATOR\""

helicopterkey = Item("Helicopter Key", "helicopter key", "chopper", "H K")
helicopterkey.description = "A metallic key with the keychain saying \"HELICOPTER\"."


######################
#Add Items to Bags
######################
washrooms.item.add(eleaccesskey)
executiveoffice.item.add(maobar)
mainoffice.item.add(notepad) 
administrationblock.item.add(adminaccesskey)
ovoffice.item.add(ovacesskey)
officeroom.item.add(exelevatorkey)
elevatortwo.item.add(maopro)
######################
#Define any variables
######################
current_room = mainoffice
inventory = Bag()
used_elekeycard = False
used_exelevatorkey = False
used_adminaccesskey = False
used_helicopterkey = False
######################
#Binds (eg “@when(“look”))
######################

@when("have the mao")
def havemao():
	inventory.add(maobar)
	inventory.add(maopro)
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
	if inventory.find(item) and inventory.find(item)==eleaccesskey and current_room == elevatortwo:
		print("You flick the elevator key against the reader. It beeps twice and all the dails become green.")
		print("The level two dial glows green and sends you up to the next level, You step out")
		current_room = administrationblock
		print(current_room)
		used_elekeycard = True
	elif inventory.find(item) and inventory.find(item)==exelevatorkey and current_room == elevatorthree:
		print("You flick the elevator key against the reader. It beeps twice and all the dials become green.")
		print("The level three button glows green and the elevator starts moving upward.")
		used_exelevatorkey = True
		current_room = ovreceptiondesk
		print(current_room)
	elif inventory.find(item) and inventory.find(item)==adminaccesskey and current_room == hallway:
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
	else:
		print("You can't use that here")


@when("look at ITEM")
def look_at_item(item):
	if item in inventory:
		print(inventory.find(item).description)

"""
@when("use elevator")
def use_elevator():
	if used_elekeycard == True:
		print("You press the number two key, and the elevator takes you up.")
	else:
		print("You don't have access to use this elevator.")
"""
#leave for later
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