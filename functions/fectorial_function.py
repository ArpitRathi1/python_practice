# Ques) Write a python program to find the fectotial of a user defined number.
# Solution-

def fect(x):
	result=1
	for i in range(1,(x+1)):
		result=result*i
	return result

n=int(input("Enter any number:"))
output=fect(n)
print("Fectorial of {} is = {}".format(n,output))
