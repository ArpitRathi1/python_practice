# Ques) Write a python program to store n number of numbers in a tuple.(Accept n form the user)
# Solution-

n=int(input("Enter how many numbers : "))
tup=()
i=1
while i<=n:
	num=float(input("Enter number : "))
	tup=tup+(num,)
	i+=1
print(tup)