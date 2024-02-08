# Ques) Write a recursive function to print numbers from N to 1.
# example for n=4
# 1
# 2
# 3
# 4


def print1toN (n):
	# Base case
	if n==0:
		return
	# Recursive case
	print1toN(n-1)
	print(n)

n=int(input("Enter n : "))
print1toN(n)