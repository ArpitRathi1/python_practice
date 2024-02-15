# Ques) Write a python function to find the user defined number is prime or not.
# Solutiion-

def prime (x):
	if x==1:
		return False
	else:
		for i in range(2,x):
			if x%i==0:
				return False
				break
		else:
			return True
			
n=int(input("Enter n : "))
for i in range (1,(n+1)):
	output=prime(i)
	if output==True:
		print(i,"is a prime number.")
	else:
		print(i,"is a non-prime number.")
