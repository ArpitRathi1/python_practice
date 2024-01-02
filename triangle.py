# Write a python program which accept three sides of triangle and check whether it is an equilateral,scalene or isosceles.
 
side_1=float(input("Enter length of side_1:"))
side_2=float(input("Enter length of side_2:"))
side_3=float(input("Enter length of side_3:"))

if side_1==side_2==side_3:
	print("It is a equilateral triangle")

if side_1!=side_2 and side_2!=side_3 and side_3!=side_1:
	print("It is a scalene triangle")

if (side_1==side_2 and side_1!=side_3 ) or (side_2==side_3 and side_2!=side_1) or (side_3==side_1 and side_3!=side_2):
	print("It is a isosceles triangle")
