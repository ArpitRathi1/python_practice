# Ques) Write a python script to reverse a string.
# Solution-

input_string=input("Enter input string : ")
reversed_string=""
for i  in range ((len(input_string)-1),-1,-1):
	reversed_string=reversed_string+input_string[i]
print("Input string : ",input_string)
print("Reversed string : ",reversed_string)
