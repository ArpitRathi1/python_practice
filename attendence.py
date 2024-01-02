# Ques) Write a python program to calculte if a student in eligible for examination or not.(required attendence=75%)

working_day=int(input("Enter total number of working days:"))
absent=int(input("Enter the number of days for which student is absent:"))

result=((working_day-absent)/working_day)*100

if result>=75:
	print("student attendence is {} so he is eligible for examination".format(result))
else:
	print("student attendence is {} so he is not eligible for examination".format(result))
