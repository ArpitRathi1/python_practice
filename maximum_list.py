# Ques) write a program to find maximum number in a list without using max function.

lst=[12,54,234,78673,42,5567,32]
maximum=lst[0]
for i in lst:
	if i > maximum:
		maximum=i
print(maximum)