# Write a python program to print table for a user defined value using for loop.

var_1=float(input("Enter any number:"))
var_y=int(input("How many iterations:"))

for i in range (1,(var_y+1)):
	print(var_1,"*",i,"=",var_1*i)
