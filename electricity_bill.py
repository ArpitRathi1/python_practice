# Q) Write a python program to calculate the electricity bill according to the number of units consumed in following criteria:
# For first 100 units-No charge.
# For next 100 units- rs 5 per unit
# After 200 units- rs 10 per unit

# solution-
# Input-1-unit.
# Output-not required.
# Process-
# 1) Take the value of number of units consumed form the user and allocate its value in unit.
# 2) If unit is less then or equal to 100 then print No charges.
# 3) Else if unit is greater then 100 and less then or equal to 200 then print Your electricity bill for this month is, (unit-100)*5.
# 4) Else print Your electricity bill for this month is, 500+(unit-200)*10.
 
unit=int(input("Enter the number or units consumed:"))

if unit<=100:
	print("No charges")

elif unit>100 and unit<=200:
	print("Your electricity bill for this month is",(unit-100)*5)

else:
	print("Your electricity bill for this month is",500+(unit-200)*10)