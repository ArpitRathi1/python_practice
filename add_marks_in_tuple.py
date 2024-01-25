# Ques) Write a python program to find sum of marks of all student stored in the given tuple.
# t1=(("Suman",35),("Arpit",75),("Ankit",50))

t1=(("Suman",35),("Arpit",75),("Ankit",50))
add=0
for i in t1:
	add=add+i[1]
print("Sum of marks is = ",add)