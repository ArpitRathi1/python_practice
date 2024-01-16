# Ques) Write a python script to delete all numbers less than 10 in a list.
# l1=[3,5,6,1,17,18,19,14,16]
# Solution-

l1=[3,5,6,1,17,18,19,14,16]
new=[]
for i in l1:
	if i>=10:
		new.append(i)
print(new)