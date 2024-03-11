# Ques) In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.
# Solution-

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
 
