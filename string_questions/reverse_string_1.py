# Ques) Write a python script to reverse a string.
# Solution-

input_string=input("Enter input string : ")
reversed_string=""
for i in range (len(input_string)):
	reversed_string=input_string[i]+reversed_string
print("Input string : ",input_string)
print("Reversed_string : ",reversed_string)
