# Ques) Write a python program which accept decimal number and display its binary number.

n=int(input("Enter decimal number:"))
binary=""
while n!=0:
	remainder=n%2
	remainder_str=str(remainder)
	binary=binary+remainder_str
	n=n//2
if n%2==1:
	binary=binary+1
final_binary=""
for j in reversed(binary):
	final_binary=final_binary+j
print("Binary number of the given number is = {}".format(final_binary))