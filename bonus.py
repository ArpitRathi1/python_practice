# Ques) Write a python program to calculate bonus according to salary and time period of service of employes.
# Solution-

salary=int(input("Enter your salary:"))
time=int(input("Enter time period of service:"))

if time>10:
	bonus=salary*(10/100)
	print("your bonus ammount is {}".format(bonus))
elif time>=6 and time<=10:
	bonus=salary*(8/100)
	print("your bonus ammount is {}".format(bonus))
else:
	bonus=salary*(5/100)
	print("your bonus ammount is {}".format(bonus))
