# Ques) Write a python program to take name and last name from user and reverse it.
# Solution-

name=input("Enter your first name : ")
last_name=input("Enter your last name : ")
output=""

for i in reversed(last_name):
	output=output+i+" "
for j in reversed(name):
	output=output+j+" "
print(output)
