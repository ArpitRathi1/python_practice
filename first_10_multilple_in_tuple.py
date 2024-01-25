# Ques) Write a python program to accpet a number from the user and store first 10 multiples of that number in a tuple.

n=int(input("Enter any number : "))
tup=()
for i in range (1,11):
	res=n*i
	tup=tup+(res,)
print(tup)