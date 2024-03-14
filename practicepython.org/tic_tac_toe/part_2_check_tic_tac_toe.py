# Ques) This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
# If a game of Tic Tac Toe is represented as a list of lists, like so:
# game = [[1, 2, 0],
# 		  [2, 1, 0],
#         [2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
# Here are some more examples to work with:
# winner_is_2 = [[2, 2, 0],
#				 [2, 1, 0],
# 				 [2, 1, 1]]

# winner_is_1 = [[1, 2, 0],
# 				 [2, 1, 0],
#                [2, 1, 1]]

# winner_is_also_1 = [[0, 1, 0],
#					  [2, 1, 0],
# 					  [2, 1, 1]]

# no_winner = [[1, 2, 0],
#			   [2, 1, 0],
# 			   [2, 1, 2]]

# also_no_winner = [[1, 2, 0],
#				    [2, 1, 0],
#				    [2, 1, 0]]
def check_grid(grid):
	# Rows
	for i in range (0,3):
		lst_1=[grid[i][0],grid[i][1],grid[i][2]]
		row=set(lst_1)
		if len(row)==1 and grid[i][0]:
			return grid[i][0]
	# columns
	for i in range(0,3):
		lst_2=[grid[0][i],grid[1][i],grid[2][i]]
		col=set(lst_2)
		if len(col)==1 and grid[0][i]:
			return grid[0][i]
	# Digonals
	lst_3=[grid[0][0],grid[1][1],grid[2][2]]
	lst_4=[grid[0][2],grid[1][1],grid[2][0]]
	digonal1=set(lst_3)
	digonal2=set(lst_4)
	if len(digonal1)==1 or len(digonal2)==1:
		return grid[1][1]


winner_is_2 = [[2, 2, 0],
				 [2, 1, 0],
 				 [2, 1, 1]]
output=check_grid(winner_is_2)
if output==1:
	print("Player 1 won the match")
elif output==2:
	print("Player 2 won the match")
elif output==None:
	print("it's a tie")


