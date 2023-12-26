# Ques) Python program to find fectorial of a user defined value using for loop.
# Solution-
# Input-1-var_1.
# Output-Result
# Process-
# 1) Take a user defined integer value and allocate its value in var_1.
# 2) Take a output result and allocate its initial value as zero.
# 3) If var_1 is equal to 0 then print fectorial of var_1 is equal to 1.
# 4) Else if var_1 is less then 0 then print Invalid number.
# 5) Else take a looping varible i in range 1 to (var_1+1) and perform operation result=result*i to update value of result for each value of i.
# 6) After complition of this loop print final result.

var_1=int(input("Enter any value:"))
result=1 

if var_1==0:
	print ("Fectorial of",var_1,"is=1")

elif var_1<0:
	print("Invalid number")

else:
	for i in range (1,(var_1+1)):
		result=result*i 
	print("Fectorial of",var_1,"is",result)
