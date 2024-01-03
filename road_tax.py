# Q) Write a python program to take user defined value of cost price of bike and calculate road tax on the bike.
# Input-1- cost_price.
# Output-Not required.
# Process-
# 1) Take user defined value of cost price of bike and allocate it in cost_price.
# 2) If cost_price is greater then 100000 then calculate the road tax on the bike on 15% and print it.
# 3) Else if cost_price is greater then 50000 and less then or equal to 100000 then calculate the road tax on the bike on 10% and print it.
# 4) Else calculate the road tax on 5% and print it.

cost_price=int(input("Enter the cost price of the bike:"))

if cost_price>100000:
	print("Road tax on this bike will be", (15/100)*cost_price)

elif cost_price>50000 and cost_price<=100000:
	print("Road tax on this bike will be", (10/100)*cost_price)

else:
	print("Road tax on this bike will be", (5/100)*cost_price)