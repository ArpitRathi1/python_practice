# Ques) Write a python program to check whether a number (accepted by the user) is present in the list or not.
l1=[1,2,3,4,5,6,7,8,9]
num=float(input("Enter any number : "))
if num in l1:
	print(num,"is present in the list")
else:
	print(num,"is not present in the list")
