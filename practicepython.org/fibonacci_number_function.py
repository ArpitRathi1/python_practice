# Ques) Write a python function that asks the user how many Fibonacci numbers to generate and then generates them.

def fibonacci (count):
	fibo=[]
	var_1=1
	var_2=1
	for i in range (count):
		fibo.append(var_1)
		result=var_1+var_2
		var_1=var_2
		var_2=result
	return fibo

count=int(input("How many fibonacci number would you like to generate ? : "))
output=fibonacci(count)
print(output)