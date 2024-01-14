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

