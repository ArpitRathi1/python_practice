# Ques) Write a program to input a number and count the occurrence of that number in the given list.
# l1=[31,21,3,12,31,56,76,5,4,21,12,34]

l1=[31,21,3,12,31,56,76,5,4,21,12,34]
num=float(input("Enter any number : "))
if num in l1:
	a=l1.count(num)
	print("{} comes {}times in the list.".format(num,a))
else:
	print("{} not found in the list".format(num))