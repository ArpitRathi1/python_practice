# Ques) Write a python function which calculates "a" raised to the power "b" using recursion.
# Solution-

def power_a_b(a,b):
	if b==0:
		return 1
	ans = a * power_a_b(a,(b-1))
	return ans

num =int(input("Enter any number:"))
power=int(input("Enter power:"))
output=power_a_b(num,power)
print ("{} raised to the power {} is = {}".format(num,power,output))
