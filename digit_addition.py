# Ques) Write a python program to display sum of digits of the number accepted from the user.

num=int(input("Enter any number:"))
addition=0
while num:
	last_digit=num%10
	addition=addition+last_digit
	num=num//10
print("Sum of digits is =",addition)