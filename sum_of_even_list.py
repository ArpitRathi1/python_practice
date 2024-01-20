# Write  a program to add all even numbers of a list.


lst=[1,2,3,4,5,6,7,8,9,10]
add_even=0
for i in lst:
	if i % 2 ==0:
		add_even=add_even+i
print("Sum of all even number in list is = ",add_even)
