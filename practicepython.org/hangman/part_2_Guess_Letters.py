# Question) Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.
# An example interaction can look like this:

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E

# solution-

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
while True:
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
		continue
	if "_" not in guess_list:
		print("you guessed currect word")
		break
