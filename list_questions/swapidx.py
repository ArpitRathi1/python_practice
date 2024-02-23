# Ques) Write a python program to swap to items in a list using index value.(index value taken by user)
# Solution-

n=int(input("Enter size of list:"))
list=[]
for i in range(n):
	num=int(input())
	list.append(num)
print(list)

idx1=int(input("Enter index 1:"))
idx2=int(input("Enter index 2:"))

temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp

print(list)
