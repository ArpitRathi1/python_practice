# Ques) Write a python script to print frequency of a number accepted from the user in the given tuple.
# T1=(12,17,18,25,19,12,18,5,19)

T1=(12,17,18,25,19,12,18,5,19)
n=float(input("Enter n : "))
if n in T1:
	print("{n} is repeated {c}times in T1".format(n=n,c=T1.count(n)))
else:
	print("{n} not found in T1".format(n=n))
