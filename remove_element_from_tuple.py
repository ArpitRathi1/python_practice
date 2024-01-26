# Ques) Write a python program to remove (accepted from the user) from the given tuple
# T1=(12,15,18,21,24,27,19)
# Solution-

T1=(12,15,18,21,24,27,19)
el=int(input("Enter the elements to be removed : "))
if el in T1:
	l=list(T1)
	l.remove(el)
	T1=tuple(l)
	print(T1)
else:
	print("Element not found.")
