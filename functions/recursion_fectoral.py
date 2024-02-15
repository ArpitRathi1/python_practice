# Ques) Write a recursive python function of calculating factorial.
# Solution-

def factorial (n):
	# Base case
	if n==0:
		return 1
	# Recursive case 
	ans=n*factorial(n-1)
	return ans

n=int(input("Enter any number:"))
output=factorial(n)
print("Fectorial of {} is = {}".format(n,output))
