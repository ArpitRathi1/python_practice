# Ques) Write a python function to find leap year.

def leap_year(n):
	if n%100==0:
		if n%400==0:
			return True
		else:
			return False
	else:
		if n%4==0:
			return True
		else:
			return False
year=int(input("Enter year :"))
output=leap_year(year)
if output==True:
	print(year,"is a leap year")
else:
	print(year,"is not a leap year")
