# Ques) Write a python program to delete all the negative numbers from the given list:
# l1=[-1,-3,9,6,0,2,-6,-11]
# Solution-

l1=[-1,-3,9,6,0,2,-6,-11]
positive=[]
for i in l1:
	if i>=0:
		positive.append(i)
print(positive)
