# Ques) Write a program to accept a number and check whether it is a perfect number or not.

num=int(input("Enter any positive integer:"))
if num<0:
	print("Invalid number.")
else:
	sum_of_divisors=0
	for i in range(1,num):
		if num % i ==0:
			sum_of_divisors=sum_of_divisors+i
if num==sum_of_divisors:
	print("{} is a perfect number.".format(num))
else:
	print("{} is not a perfect number.".format(num))