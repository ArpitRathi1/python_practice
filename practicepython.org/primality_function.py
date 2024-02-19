# Ques) Ask the user for a number and determine whether the number is prime or not.

def primality(n):
	if n==1:
		return False
	else:
		for i in range(2,n):
			if n%i==0:
				return False
				break
		else:
			return True
n=int(input("Enter any number :"))
output=primality(n)
if output==True:
	print(n,"is a prime number.")
else:
	print(n,"is a non-prime number.")
