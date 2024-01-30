# Ques)  Write a program to print all prime number fall between two numbers including both.(accept two numbers from user)
# Solution-

num_1=int(input("Enter first number:"))
num_2=int(input("Enter second number:"))
extra=[]
prime=[]
non_prime=[]
for i in range(num_1,(num_2+1)):
    if i == 0:
        extra.append(i)
    elif i == 1:
        non_prime.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                non_prime.append(i)
                break
        else:
            prime.append(i)
print("Prime number-",prime)
print("Non-prime-",non_prime)
print("Neither prime nor Non-prime-",extra)
