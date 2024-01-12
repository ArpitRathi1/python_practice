# Ques) Write a python script to convert any user defined to camelcase.
# Solution-

input_str=input("Enter input string : ")
start=input_str[0].lower()
mid=input_str[1:(len(input_str)-1)].upper()
end=input_str[(len(input_str)-1)].lower()
print(start+mid+end)
