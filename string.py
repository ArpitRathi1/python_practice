# Creating string.
name_1='Arpit Rathi'
name_2="Kapil Malviya"
name_3='''Shubham Raikwar'''
print(name_1,name_2,name_3)
print(type(name_1))
print(type(name_2))
print(type(name_3))

# Assigning multiline string to a variable.
paraghaph='''This is a multiline string.
you can write within triple quates.'''
print (paraghaph)

# Array like indexing.
text="Hello, World"
print(text[0])
print(text[4])
print(text[-1])

# Traverse a string.
text="Hello, World"
# using for loop.
for i in text:
	print(i)

# Finding length of a string.
name='Arpit'
print(len(name))

# Find a chr/substring in a string.
print(name_1.find("A"))
print(name_1.find("z")) # -1 means that it is not present in the given string.

# if you find a sub string it will give you its starting point.
print(name_1.find("pit"))

# Slicing of a string.
st_1="abcdef"
# If we want a sub string from c to d.
st_2=st_1[2:4]
print(st_2)
# Slice from the start- if we want a sub string from a to c.
st_3=st_1[0:3]
print(st_3)
# or 
st_4=st_1[:3]
print(st_4)
# Slice till end - if we want a sub string from d to f.
st_5=st_1[3:]
print(st_5)
# or 
st_6=st_1[-3:]