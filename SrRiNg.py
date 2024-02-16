# Ques) Write a python script to convert a user defined string into the following manner:
# input : string
# output : StRiNg

input_string=input("Enter input string : ")
output_string=""
for i in range (len(input_string)):
	if i==0 or i%2==0:
		var=input_string[i].upper()
		output_string=output_string+var
	else:
		var=input_string[i].lower()
		output_string=output_string+var
print("Input string : ",input_string)
print("output string : ",output_string)