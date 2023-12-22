# Ques) Write a program to find the user defined number is even or odd.
# Input-1- num
# Output- 1- result
# Process-
# 1) Take a user defined integer number and allocate its value in num.
# 2) Find the remainder of the number given by the user by dividing it by 2 and then allocate its value in result.
# 3) If the value of result is equal to 0 then print number is even.
# 4) else print number is odd.

num=int(input("Enter any number:"))

result=num%2

if result==0:
	print(num,"is Even")
else:
	print(num,"is Odd")
