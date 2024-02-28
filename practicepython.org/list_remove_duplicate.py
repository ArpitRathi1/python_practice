# Ques) Write a program function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
# 1)Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Solution-

def removing_duplicate_1(lst):
	new_list=[]
	for i in lst:
		if i not in new_list:
			new_list.append(i)
	return new_list

def removing_duplicate_2(lst):
	lst_set=set(lst)
	new_list=list(lst_set)
	return new_list

lst=[1,2,1,4,1,4,2,7,5,7,6]
output=removing_duplicate_2(lst)
print(output)
