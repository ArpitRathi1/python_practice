# Ques) Write a python program to create a calculator using if else ladder.
# Solution-

num_1=float(input("Enter num_1:"))
num_2=float(input("Enter num_2:"))

oprator=input("Enter oprator:")

if oprator=="+":
	print("Addtion is=",num_1+num_2)

elif oprator=="-":
	print("Difference is=",num_1-num_2)

elif oprator=="*":
	print("Multiplication is=",num_1*num_2)

elif oprator=="/":
	print("Division is=",num_1/num_2)

elif oprator=="//":
	print("Floor division is=",num_1//num_2)

elif oprator=="%":
	print("Remainder is=",num_1%num_2)

elif oprator=="**":
	print("result is=",num_1**num_2)

else:
	print("Invalid oprator")

