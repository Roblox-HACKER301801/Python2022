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
mainoffice = Room("""Your inside a gloomy lobby to the tower that you work at. The smell of plastic fills your nose. """)
elevatortwo = Room("""You've entered the elevator, all you see is a greasy set of dails and a Mao Zedong poster, The access reader glows red. You need a keycard.""")
elevatorthree = Room("""You enter another elevator to the floor above yours. The faint radio filled with chinese propaganda fills the room.""")

washrooms = Room("""You enter a bathroom stall. It smells awful and all there is to fill in the darkness are some Mao
zedong propaganda, You see an elevator keycard near one of the sinks.""")
officeroom = Room("""A room filled with computers and desks.""")
administrationblock = Room("""A small room with a single desk and computer on it. Seems quite valuable
since it has warning sign on it, You also see an admin keycard on the desk""")
#overseers office part:
ovreceptiondesk = Room("""You enter  room which contains a computer and a seat. Nicely named \"Overseers reception\".""")
ovoffice = Room("""You enter the huge room, the only one with some sort of design, its got a casset player, and the most modern
pc setup, and a massive painting of Mao zedong on the wall.""")
hallway = Room("""You enter a well-lit hallway with pictures of Mao-Zedong to both sides of your vision.""")
executiveoffice = Room("""You enter a more brighter room, within it are multiple smaller cubicals. You catch a glimps of something that looks like a chocolate bar on one of the desks.""")
executivebathroom = Room("""You enter a stylish bathroom, A nice smooth smell of fresh air """)
helicopter = Room("""You open the door and enter the helipad, a black bullet proof helicopter is infront of you,
with the chinese insigmia on the side of it.""")
######################
#Define Connections
######################
mainoffice.north = elevatortwo
mainoffice.east = washrooms
elevatortwo.north = administrationblock
administrationblock.west = officeroom
administrationblock.north = elevatorthree
elevatorthree.north = ovreceptiondesk
ovreceptiondesk.east = executiveoffice
ovreceptiondesk.north = hallway
hallway.north = ovoffice
ovoffice.east = executivebathroom
ovoffice.west = helicopter
######################
#Define Items
######################
eleaccesskey = Item("elevator key","elevator keycard","elevator Key","elevator Keycard")
eleaccesskey.description = "The keycard with a bold text \"elevator\" on its side."

adminaccesskey = Item("admin key", "admin Key", "Admin Key", "Administration Keycard")
adminaccesskey.description = "A keycard with a bold text \"admin\" on its side"

ovacesskey = Item("overseer key", "ov key", "overseer Key", "ov Key")
ovacesskey.description = "A keycard with a bold text \"overseer\" on its side, with a text on its other side being \"ACCESS TO EVERYTHING\""

easteregg = Item("EASTER", "easter", "EGG", "egg")
easteregg.description = "You say the word \"easter\" and feel something in your pocket... its an overseer card"

maobar = Item("mao bar","Mao Bar", "Chocolate", "chocolate", "choco", "Choco")
maobar.description = "A small bar of chocolate with Mao zedong's face on it. Ingrediants: LSD, Cocaine, Lean, p, weed, chocolate mix, flour, sugar, baking soda, vinahe, plastic, acid, more lean."

maopro = Item("propaganda", "poster")
maopro.description = "A poster with Mao zedong's massive face glearing back at you. Under the face it says \"For china!\""

notepad = Item("Note", "note", "notepad", "Notepad")
notepad.description = "A notepad with most of the pages scribbled with unreadable chinese. One of it says \"EVACUATION: Due to multiple riots, all personnel are to evacuate via the main enterance.\""
######################
#Add Items to Bags
######################
washrooms.item.add(eleaccesskey)
executiveoffice.item.add(maobar)
mainoffice.item.add(notepad) 
administrationblock.item.add(adminaccesskey)
######################
#Define any variables
######################
current_room = mainoffice
inventory = Bag()
used_elekeycard = False
######################
#Binds (eg “@when(“look”))
######################
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
	if inventory.find(item) and inventory.find(item)==eleaccesskey and current_room == elevatortwo or elevatorthree:
		print("You flick the elevator key against the reader. It beeps twice and all the dails become green.")
		print("The level two dail glows green and sends you up to the next level.") 
		used_elekeycard = True
	if inventory.find(item) and inventory.find(item)==maobar:
		print("You tear the wrapper and see the chocolate, ingraved is mao zedongs face. You snap a piece off and slowly chew it.")
		print("It's disgusting but you fight through the disgusting taste.") 
	else:
		print("You can't use that here")
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