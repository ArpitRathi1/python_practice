# Write a program to delete all the repeated numbers in a list.

lst=[1,2,3,4,5,6,2,4,1,8]
new_list=[]
for i in lst:
	if i not in new_list:
		new_list.append(i)
print (new_list)
