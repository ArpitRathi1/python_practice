# Ques) Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# Rule no. 1-Rock beats scissors
# Rule no. 2-Scissors beats paper
# Rule no. 3-Paper beats rock
# Solution-

choice=True
while choice==True:
	a=input("Choose rock,paper or scissor for Player 1 : ")
	b=input("Choose rock,paper or scissor for Player 2 : ")

	if a.lower()=="rock" and b.lower()=="scissor":	
		print("Player 1 win this match.")
	elif b.lower()=="rock" and a.lower()=="scissor":
		print("Player 2 win this match")
	elif a.lower()=="scissor" and b.lower()=="paper":
		print("Player 1 win this match.")
	elif b.lower()=="scissor" and a.lower()=="paper":
		print("Player 2 win this match")
	elif a.lower()=="paper" and b.lower()=="rock":
		print("Player 1 win this match.")
	elif b.lower()=="paper" and a.lower()=="rock":
		print("Player 2 win this match")
	elif a.lower()==b.lower():
		print("It's a tie")
	else:
		print("Invalid input")
	user_choice=input("Press Y to play again or any key to shop : ")
	if user_choice.lower()=="y":
		choice=True
	else:
		choice=False
print("Exiting the game.")
