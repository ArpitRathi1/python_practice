# Ques) Write a python program to find fectorial of a user defined integer number.
# Solution-

var=int(input("Enter any number:"))
if var==0:
	print("Fectorial of",var,"is=1")
elif var<0:
	print("Invalid number")
else:
	i=1
	result=1
	while i<=var:
		result=result*i
		i+=1
	print("Fectorial of",var,"is=",result)
