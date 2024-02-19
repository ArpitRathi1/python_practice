# Ques)Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# Extras:
# 1) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2) Write this in one line of Python.
# 3) Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
# Solution-

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Printing number less than 5.
for i in a:
  if i<5:
    print(i)

# Extra 1-
b=[]
for i in a:
  if i<5:
    b.append(i)
print(b)

# Extra 2-
c=[i for i in a if i<5]
print(c)

# Extra 3-
num=float(input("Enter number : "))
d=[i for i in a if i<num]
print(c)
