# Ques) Write a python script to swap two numeric variable without using a third varible.

a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
print("a :",a)
print("b ;",b)

a=a+b
b=a-b
a=a-b

print("a :",a)
print("b :",b)