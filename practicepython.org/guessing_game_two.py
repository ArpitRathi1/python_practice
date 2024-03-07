# Ques) This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.

number=int(input("Enter a number between 1 to 100 : "))
count=0
while True:
	if number==50:
		count+=1
		print("Program guessed the currect number in",count,"attempt.")
		break
	elif number<50:
		for i in range (1,50):
			if i!=number:
				count+=1
			else:
				count+=1
				print("Program guessed the currect number in",count,"attempt.")
				break
		break
	else:
		for i in range(51,101):
			if i!=number:
				count+=1
			else:
				count+=1
				print("Program guessed the currect number in",count,"attempt.")
				break
		break