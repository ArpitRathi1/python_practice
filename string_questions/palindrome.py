# Ques) Write a python program to check the given input is a palindrome or not.
# Solution-

input_string=input("Enter input_string:")
reverse=""
for i in reversed(input_string):
	reverse=reverse+i
print(reverse)
if input_string==reverse:
	print("It is a palindrome.")
else:
	print("It is not a palindrome.")
