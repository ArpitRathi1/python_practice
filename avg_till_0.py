# Write a python program that keeps accepting numbers from the user untill user enters zero and display sum and average of all numbers.

num=1
add=0
i=-1
while num:
	num=float(input("Enter any number:")) 
	add=add+num
	i+=1
print("Addition",add)
print("Average",add/i)