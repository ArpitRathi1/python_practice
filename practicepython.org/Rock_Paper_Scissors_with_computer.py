# Ques) Write a python program to play Rock-Paper_Scissors with computer.
# Solution-

import random

user_win=0
computer_win=0
options=["rock","paper","scissors"]


while True:
	user_choice=input("Choose between Rock/Paper/Scissors or Q to quit the game : ").lower()
	if user_choice=="q":
		break
	if user_choice not in options:
		print("Enter valid input")
		continue
	random_number=random.randint(0,2)
	# 1: rock , 2: paper , 3:scissors
	computer_choice=options[random_number].lower()
	print("Computer Picked : ",computer_choice)
	if user_choice=="rock" and computer_choice=="scissors":
		user_win+=1
		print("You won")
	elif user_choice=="paper" and computer_choice=="rock":
		user_win+=1
		print("You won")
	elif user_choice=="scissors" and computer_choice=="paper":
		user_win+=1
		print("You won")
	elif user_choice==computer_choice:
		print("It's a tie")
	else:
		computer_win+=1
		print("Computer won")
print("You won {} times.".format(user_win))
print("Computer won {} times".format(computer_win))
print("Goodbye!!")
