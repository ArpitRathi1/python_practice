# Ques) Write a python function to calculate sum 1 to n.

def sum1ToN (n):
	add=0
	for i in range (1,(n+1)):
		add=add+i
	return add

n=int(input("Enter n : "))
output=sum1ToN(n)
print(output)