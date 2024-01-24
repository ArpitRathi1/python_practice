# Ques) Write a python script to add three numbers form the user and insert it at the end of the given series t1.
# Solution-

t1=(1,2,3,4,5,6)
t2=()
for i in range (3):
	num=float(input("Enter any number to add in tuple : "))
	t2=t2+(num,)
t1=t1+t2
print(t1)