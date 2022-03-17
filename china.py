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
elevatortwo = Room("""You've entered the elevator, all you see is a greasy set of dails and a Mao Zedong poster""")
elevatorthree = Room("""You enter another elevator to the floor above yours. The faint radio filled with chinese propaganda fills the room.""")

washrooms = Room("""You enter a bathroom stall. It smells awful and all there is to fill in the darkness are some Mao
zedong propaganda, You see a keycard near one of the sinks.""")
officeroom = Room("""A room filled with computers and desks. """)
administrationblock = Room("""A small room with a single desk and computer on it. Seems quite valuable
since it has warning sign on it""")
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

######################
#Add Items to Bags
######################
washrooms.item.add(eleaccesskey)
executiveoffice.item.add(maobar)

######################
#Define any variables
######################
current_room = mainoffice
inventory = Bag()
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