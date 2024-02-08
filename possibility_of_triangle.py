# Ques) Write a python program to check a triangle is possible or not with the given length of sides.
# Solution-

side_1=float(input("Enter length of side 1:"))
side_2=float(input("Enter length of side 2:"))
side_3=float(input("Enter length of side 3:"))

if (side_1+side_2)>side_3 and (side_2+side_3)>side_1 and (side_3+side_1)>side_2:
	print("Making of a triangle is possible with is sides.")
else:
	print("Making of a triangle is not possible with is sides.")
