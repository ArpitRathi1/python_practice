# Ques) Write a python program which accept the kilometer and calculate bill according to following criteria:
# First 10 km - rs 11/km
# Next 90 km  - rs 10/km
# After that  - rs 9/km
# Solution-

km=float(input("Enter the number of kilometer car drove:"))

if km<=10:
	bill=km*11
	print("your bill ammount is",bill)

elif km>10 and km<=100:
	bill=110+(km-10)*10
	print("your bill ammount is",bill)

else:
	bill=(110+900)+(km-100)*9
	print("your bill ammount is",bill)
