# Ques) Write a python program to print fibonacci series.
# Solution-

n=int(input("Enter n:"))
num_1=0
num_2=1
for i in range(n):
	print(num_1)
	res=num_1+num_2
	num_1=num_2
	num_2=res
