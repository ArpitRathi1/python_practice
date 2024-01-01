# Accept the sex ("M","F") , number of days and display the wages accorodingly:
# Age               Sex               Wages/day
# >=18 and <30      M                 700
#                   F                 750
# >=30 and <=40     M                 800
#                   F                 850 
# Solution-

age=int(input("Enter age:"))
sex=input("Enter sex 'M or F':")
num=int(input("Enter number of working days:"))

if age>=18 and age<30:
	if sex.upper()=="M":
		wage=num*700
		print("Total wage is",wage)
	else:
		wage=num*750
		print("Total wage is",wage)
if age>=30 and age<=40:
	if sex.upper()=="M":
		wage=num*800
		print("Total wage is",wage)
	else:
		wage=num*850
		print("Total wage is",wage)
else:
	print ("Enter apporopriate age")

