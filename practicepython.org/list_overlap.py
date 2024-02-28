# Ques) Take two lists, say for example these two:
  # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
# 1)Write this in one line of Python.
# Solution-

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a:
  if i in b:
    c.append(i)
    c_set=set(c)
    c_lst=list(c_set)
print(c_lst)

# Extra 1-
d=[i for i in a if i in b]
d_set=set(d)
d_lst=list(d_set)
print(d_lst)
