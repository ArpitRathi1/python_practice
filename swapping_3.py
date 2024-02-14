# Ques) Write a python program to swap two numbers without using a third variable.
# Solution-

a=int(input("Enter number one : "))
b=int(input("Enter number two : "))

print("First number : ",a)
print("Second number : ",b)

a=a+b
b=a-b
a=a-b

print("First number : ",a)
print("Second number : ",b)
