#1
"""
icecream = int(input("How many ice-creams do you want?\n")) 
if icecream <=10: 
	print(f"You have ordered {icecream}, they should be read in 4 minutes")
else:
	print(f"Unfortunately we cannot make {icecream} icecream's. We would run out") 
#2
fuel = int(input("How much meters are you planning to travel?\n")) 
if fuel <=200:
	print(f"Great, you should have enough fuel for the trip") 
else:
	print(f"You may need to fuel up your car during this travel, \nor you may need to know if there will be any gasstations on your way.") 
#3
age = int(input("How old are you?\n")) 
if age >= 18:
	print("You are old enough") 
else:
	print("You are not old enough") 
#4
fav_movie = input("What is your fav movie?\n") 
if fav_movie == "lord of the rings":
	print("You have great taste") 
else:
	print("lord of the rings is a better movie!.") 
#5
darth_plagueis = input("Have you heard of the story of darth plagueis?\n")
if darth_plagueis == "no" or darth_plagueis == "No":
	print("\"Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.\"- Sheev Palpatine or Darth Sidious")
else: 
	print("So you know it already. Good.")
#6	
mel_gibson = input("Do you know who directed passion of the christ?") 
if mel_gibson == "Mel Gibson" or mel_gibson == "mel gibson":
	print("Correct")
else:
	print("WRONG, Mel Gibson had directed the movie!")
"""
#7
score = 0 
print("Welcome to the CCP quiz, Answer these 5 questions to increase your social credit score from 0 to 5! You are being monitored while doing this quiz.") 
question_1 = input("What do you think about the party? Describe it in one word.") 
if question_1 == "Good" or question_1 == "good":
	score= score + 1
	print(f"Good answer you have increased your score by 1, New score: {score}") 
else:
	score= score - 1
	print(f"You are incorrect. No new score. Your score is now: {score}")
question_2 = input("Question 2:\n Are you an active person of the party?")
if question_2 == "Yes" or question_2 == "yes":
	score= score + 1
	print(f"Correct answer. Your score is now: {score}")
else:
	score= score - 1
	print(f"You are wrong, score has been decreased by 1. New score: {score}")  
question_3 =int(input("Question 3:\n How many hours have you worked in the past 2 weeks?"))
if question_3 >= 12:
	score= score - 1
	print(f"You have worked for a very low amount of hours. Unacceptable. \n New credit score: {score}")
else:
	score= score +1
	print(f"Correct answer, Your hard work has been noted")	
#finish off.