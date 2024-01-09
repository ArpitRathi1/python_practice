# Ques) Write a program to take a user defined year and check it is a leap year or not.

year=int(input("Enter any year:"))

if year%100==0:
	if year%400==0:
		print(year,"is leap year")
	else:
		print(year,"is not a leap year")
else:
	if year%4==0:
		print(year,"is leap year")
	else:
		print(year,"is not a leap year")
