#import all the functions from adventurelib
from adventurelib import *



#rooms
Room.item = Bag()

space = Room(""" You are drifting in space. You see a space ship""")
airlock = Room("You are in an airlock") 
cargo = Room("You are in the cargo bay")
docking = Room("You are in the docking bay") 
hallway = Room("You are in a hallway")
bridge = Room("You are at the bridge. There is a body here") 
quaters = Room("You are in the main quaters. There is a locker.") 
mess_hall = Room("You are at a messey hall")
escape_pods = Room("You are at the escape pods")

#room connections
docking.west = cargo
hallway.north = cargo
hallway.east = bridge
hallway.south = mess_hall
hallway.west = airlock
bridge.south = escape_pods 
mess_hall.west = quaters 
quaters.north = airlock

#items
keycard = Item("A red Keycard", "keycard", "card", "key", "red keycard")
keycard.description = "You look at the side of the card and see the escape lable on it"

note = Item("A scribbled note","note","paper","code")
note.description = "You look at the note. The numbers 2,3,5,4 are scribbled on it" 

#add items to room
quaters.item.add(note)


#variables
current_room = space
inventory = Bag()
body_searched = False
used_keycard = False

#binds
@when("jump")
def jump():
	print("You jump")


@when("enter airlock")
@when("enter spaceship") 
@when("enter ship") 
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
	else: 
		print("There is no airlock here.") 
	print(current_room)
@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#checks if the current room list of exits has 
		#the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way") 
@when("look")
def look():
	print(current_room)
	print(current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item) 
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def get_item(item):
	#check if item is in room
	#take it out of room
	#put into inventory 
	#otherwise tell user there is no item
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You picked up the {item}") 
	else:
		print(f"You don't see a {item}") 


@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

@when("search body")
@when("search man")
@when("look at body") 
def search_body():
	if current_room == bridge and body_searched == False:
		print("you search the body and a red keycard falls to the floor") 
		current_room.items.add(keycard)
		body_searched = True
	elif current_room == bridge and body_searched == True:
		print("You already searched the body")
	else:
		print("There is no body here to search")


@when("use ITEM")
def use(item):
	if item == keycard and current_room == bridge:
		print("You use the keycard and the escape pod slides open") 
		print("The escape pod stands open to the south") 
		used_keycard = True 
		bridge. south = escape_pods 
	else:
		print("You can't use that here") 

@when("type code") 
def escape_pod_win():
	if note in inventory:
		if current_room == escape_pods:
			print("You enter the code and escape. You win")
		else:
			print("There is no where to enter the code")
	else:
		print("You don't have the code. You can't just guess it.")

































































































#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE 
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
#start the main loop

if __name__ == '__main__':
	main()