# Ques)Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
# solution-

def drow_horizontal_line():
	print(" ---" * n)
def drow_vertical_line():
	print("|   " * (n+1))


n=int(input("Enter size of game board : "))
for i in range (n):
	drow_horizontal_line()
	drow_vertical_line()
drow_horizontal_line()
