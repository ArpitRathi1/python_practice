# Ques) Write a python program to print the greatest number among 3 user defined numbers.
# Solution-

n1=float(input("Enter number one:"))
n2=float(input("Enter number two:"))
n3=float(input("Enter number three:"))

if n1>=n2 and n1>=n3:
	print(n1,"is the greatest number")
elif n2>=n1 and n2>=n3:
	print(n2,"is the greatest number")
else:
	print(n3,"is the greatest number")
