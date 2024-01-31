# Ques) Write a program to print table of a user defined number using while loop.
# solution-

var_1=float(input("Enter any number:"))
var_y=int(input("How many iterations:"))

i=1
while i<=var_y:
	print(var_1,"*",i,"=",var_1*i)
	i+=1
