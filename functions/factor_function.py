# Ques) Write a python function to find factors of a number.

def factor (num):
	factors=[]
	for i in range(1,(num+1)):
		if num%i==0:
			factors.append(i)
	return factors

n=int(input("Enter number : "))
output=factor(n)
print("factors of ",n,"is : ",output)