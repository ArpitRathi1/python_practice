num=int(input("Enter any number:"))

if num==0:
	print(num,"is neither prime nor non-prime.")
elif num==1:
	print(num,"is a non-prime number.")
else:
	i=2
	while i<num:
		if num%i==0:
			print(num,"is a non-prime number.")
			break
		i+=1
	else:
		print(num,"is a prime number.")