# Ques) Write a python program to to display sum of all numbers in the given tuple:
# t1=(1,2,3,"A",4,"sun")

t1=(1,2,3,"A",4,"sun")
add=0
for i in t1:
	if str(i).isdigit():
		add=add+i
print("Sum of all digit in the given tuple : ",add)
