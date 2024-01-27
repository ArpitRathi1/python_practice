# Write a python program to display prime numbers below any number accept from user.

n=int(input("Enter n:"))
prime=[]
non_prime=[]
extra=[]
for i in range(n):
	if i==0:
		extra.append(i)
	elif i==1:
		non_prime.append(i)
	else:
		for j in range(2,i):
			if i%j==0:
				non_prime.append(i)
				break
		else:
			prime.append(i)
print("Prime numbers from 1 to {} is : {}".format(n,prime))
print("Non prime number from 1 to {} is : {}".format(n,non_prime))
print("Neither Prime nor Non prime : {}".format(extra))