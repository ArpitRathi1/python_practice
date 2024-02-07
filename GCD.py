def GCD (x,y):
	if x>y:
		small=y
	else:
		small=x
	for i in range(1,(small+1)):
		if x%i==0 and y%i==0:
			GCD=i
	return GCD
	
n=int(input("Enter first number : "))
m=int(input("Enter second number : "))
output=GCD(n,m)
print(output)
