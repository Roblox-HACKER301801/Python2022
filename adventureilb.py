#import all the functions from adventurelib
from adventurelib import *



#rooms
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

#variables
current_room = space






















#EVERYTHING GOES ABOVE HERE - DO NOT CHANGE 
#ANYTHING BELOW THIS LINE
#the main function
def main():
	print(current_room)
	start()
#start the main loop

if __name__ == '__main__':
	main()
