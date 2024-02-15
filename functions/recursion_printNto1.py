# Ques) Write a recursive function to print numbers from N to 1.
# example for n=4
# 4
# 3
# 2
# 1
# Solution-

def printNto1 (n):
	# Base case
	if n==0:
		return          # it means dont do anything just return.
	print(n)
	# Recurive case
	printNto1(n-1)

n=int(input("Enter n:"))
output=printNto1(n)
