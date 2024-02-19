# Ques) Write a function that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
# Solution-

def list_ends(lst):
	b=[lst[0],lst[-1]]
	return b

a = [5, 10, 15, 20, 25]
print(list_ends(a))
