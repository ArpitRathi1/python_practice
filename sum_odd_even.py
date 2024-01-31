# Ques) Write a python program to display sum of all odd and even number fall between two numbers including both.
# Solution-

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

even=0
odd=0

for i in range(n1,(n2+1)):
	if i % 2 == 0:
		even=even+i
	else:
		odd=odd+i 

print("Sum of all even number fall between {} and {} is = {}".format(n1,n2,even))
print("Sum of all odd number fall between {} and {} is = {}".format(n1,n2,odd))
