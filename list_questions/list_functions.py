# Properties of list.
# 1) Indexed.
# 2) Ordered.
# 3) Mutable.
# 4) Duplicates are allowed.
# 5) List can be of any datatype.

# Creation of a list.
l1=["Arpit","Ankit",12,18,27,9.8]
l2=[1,2,3,4,5]

print(l1)              # To print list.
print(type(l1))        # To check type.
print(len(l1))         # To check length.  

# To access item of a list.
print(l1[1])           # Positive indexing.
print(l1[-1])          # Negatiive indexing.
print(l1[0:3])         # To access a range in the list.

# To add something in list.
l1.append(10)          # To add something at last.
print(l1)
l1.insert(2,40)        # To add somrthing at an specific index.
print(l1)
l1.extend(l2)          # To add another list.
print(l1)

# To remove item from a list.
l1.remove(12)          # To remove specific item from from a list.
print(l1)              # remove() function takes item as in argument and it takes only one argument.
l1.pop(1)              # To remove item at an specific index
print(l1)              # pop() function takes index as an argument and it takes only one argument.
del l1[1]              # To remove item at an specific index.
print(l1)              
del l1[7:]             # del can also remove a range in a list
print(l1)

# Unpacking a list.
a,b,c,d,e,f,g=l1       # Number of variable should be equal to number or item in a list.
print(a)
print(g)

# To change item in a list.
l1[6]=5                # To change item at an specific index.
print(l1) 
l1[1:3]=6,12           # To change item at a range.
print(l1)

# List concatination.
l1=l1+l2
print(l1)

# List replication.
l2=l2*3
print(l2)

# Sorting of list.
l3=[2,5,1,9,6,0,4]     # To arrange in ascending order.
l3.sort()
print(l3)
l3.sort(reverse=True)  # To arrange in desending order.
print(l3)

# To reverse a list.
l3.reverse()
print(l3)

# List comprehension-
l4=[1,2,3,4,5,6,7,8,9]
# If you want to make a list from the item of list l4 having number more than 4.
l5=[i for i in l4 if i>4]
print(l5)

# To copy a list
l6=l5.copy()
print(l6)

# To find index of a item.
print(l1.index(6)) 