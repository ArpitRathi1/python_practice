# Ques) Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def element_search(lst,element):
	lst.sort()
	if element in lst:
		return True
	else:
		return False