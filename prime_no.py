# Ques) Write a program to check a number is a prime number or not.

num=int(input("Enter any number:"))

if num==0:
	print(num,"is a neither prime nor non-prime")
elif num==1:
	print(num,"is a non-prime number.")
elif num<0:
	print("Invalid number.")
else:
	for i in range(2,num):
		if num%i==0:
			print(num,"is a non-prime number.")
			break
	else:
		print(num,"is a prime mumber.")
