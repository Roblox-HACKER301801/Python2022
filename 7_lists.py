#1
number = ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34"]
print(number)
#2
fruit = ["Apple", "banana", "grape", "tamato","Strawberry"]
print(fruit) 
#3
youtubers = ["Mrbeast","Russia_gamers", "Walterbonk","darkstrike-GAMING72"]
print(youtubers)
#4
song = []
song.append("Rasputin")
song.append("[庄学忠] 懂你 -- 新民歌红 ")
song.append("The red sun in our hearts")
song.append("Discord call sound 10 hours")
#5
"""
book = []
book.append(input("Please give me a name of a book\n"))
book.append(input("Please give me a name of a book\n"))
book.append(input("Please give me a name of a book\n"))
book.append(input("Please give me a name of a book\n"))
book.append(input("Please give me a name of a book\n"))
print(book)
"""
#6
print("Hi, welcome to Ice Cream Maker")
order_complete = False
toppings_list = []
while order_complete == False:
	topping = input("What topping? - push enter to finish")
	if topping == "": 
		print("Order Done")
		order_complete = True
	elif topping in toppings_list:
		print("You already have that topping")
	else: 
		print("Great, adding it to the list")
toppings_list.append(topping)

print("Here are your toppings")

print(",".join(toppings_list))