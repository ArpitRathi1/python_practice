# Ques) Write a python program to take tempreture based ordering.

# Solution-
# Input-1- temp
# Output- not required
# Process-
# 1) Take a user defined value of tempreture and allocate it in temp.
# 2) If value in temp is less then or equal to 20 then print I will have coffee.
# 3) Else if value in temp is more then 20 and less then or equal to 25 then print I will have tea.
# 4) Else print I will have cold coffee.

temp=float(input("Enter temp:"))

if temp<=20:
	print("I will have coffee")

elif temp>20 and temp<=25:
	print("I will have tea")

else:
	print("I will have cold coffee")
