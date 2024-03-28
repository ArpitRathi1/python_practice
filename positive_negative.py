# Ques) Write a program to check a check a user defined number is positive or negative.
# Solution-
# Input-1-number.
# output-not required.
# process-
# 1) Take a user defined number and allocate its value in number variable.
# 2) If number is equal to zero then print 0 is neither positive nor negative.
# 3) If number is greater then zero then print the number is positive.
# 4) Else print number is negative.

number=float(input("Enter any number:"))

if number==0:
	print("0 is neither positive nor negative")
elif number>0:
	print("the number is positive")
else:
	print("the number is negative")
