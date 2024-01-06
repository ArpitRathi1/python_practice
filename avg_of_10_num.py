# Ques) Write a python program which accept 10 numbers and display their average.
# Solution-

numbers=[]
for i in range (10):
	num=float(input("Enter number:"))
	numbers.append(num)
print(numbers)
addition=sum(numbers)
print("Average of following 10 numbers is =",addition/10)
