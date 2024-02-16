# Write a python script to print fibonacci series by a recursive function.

def fibonacci(n):
	if n==1:        # Base case
		return 0
	elif n==2:      # Base case
		return 1
	else:           # Recursive case
		return (fibonacci(n-1)+fibonacci(n-2))

n=int(input("Enter n:"))
for i in range (1,(n+1)):
	print (fibonacci(i))