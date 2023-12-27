# Write a python program to display product of digits of the number accepted from the user.

num=int(input("Enter any number:"))
product=1
while num:
	last_digit=num%10
	product=product*last_digit
	num=num//10
print("Product of digits of is =",product)