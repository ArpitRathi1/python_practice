# Write a recursive function to print sum from 1 to n.

def sum1toN (n):
	# Base case
	if n==0:
		return 0
	# Recursive case
	ans=n+sum1toN(n-1)
	return ans

n=int(input("Enter n:"))
output=sum1toN(n)
print("Sum from 1 to {} is = {}".format(n,output))