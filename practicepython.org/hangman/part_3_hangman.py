# Question) This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.
# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# 1) Only let the user guess 6 times, and tell the user how many guesses they have left.
# 2) Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

import random

def pick_word():
	sowpods_list=[]
	f1=open("sowpods.txt","r")
	line=f1.readlines()
	for i in line:
		a=i.replace("\n","")
		sowpods_list.append(a)
	random_choice=random.choice(sowpods_list)
	return random_choice

word=pick_word()
guess="_"*len(word)
word_list=list(word)
guess_list=list(guess)
incurrect_guess=0
print(word)
while incurrect_guess<6:
	letter=input("Guess letter : ").upper()
	if letter in word_list:
		for i in word_list:
			if i==letter:
				index=word_list.index(i)
				guess_list[index]=i
				word_list[index]=i.lower()
				print(guess_list)
				print("Currect Guess")
				continue
	elif letter.lower() in word_list:
		print("Already guessed")
	else:
		print("Incurrect guess")
		incurrect_guess=incurrect_guess+1
		print("Now you have only",(6 - incurrect_guess),"incurrect guesses.")
		if incurrect_guess==6:
			print("you lost the game")
	if "_" not in guess_list:
		print("you guessed currect word")
		break