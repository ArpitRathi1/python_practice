# Ques)Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# 1)Ask user if he want to play agian or not.
# 2)Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
choice=True
while choice==True:
	a=random.randint(1,9)
	g=0
	c=0
	while g!=a:
		g=int(input("Enter your guess : "))
		if g>=1 and g<=9:
			if g<a:
				c+=1
				print("Too low")
			elif g>a:
				c+=1
				print("Too high")
			else:
				c+=1
				print("Congratulation!! you guess the right number in only in",c,"attempts")
		else:
			print("Your input must be between 1 and 9 inclusive")
	user_choice=input("Do you want to play again?\nPress Y to play again \nPress any key to exit : ")
	if user_choice.lower()=="y":
		choice=True
	else:
		choice=False
		print("Exiting the game")
