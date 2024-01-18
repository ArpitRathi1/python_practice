# Ques) Write a python program to accept 10 numbers from the user and seprate the number in two list odd and even.

input_numbers=[]
for i in range (10):
	num=int(input("Enter any number : "))
	input_numbers.append(num)
print("Input numbers : ",input_numbers)
even=[]
odd=[]
for j in input_numbers:
	if j%2==0:
		even.append(j)
	else:
		odd.append(j)
print("Even numbers : ",even)
print("Odd numbers : ",odd)
