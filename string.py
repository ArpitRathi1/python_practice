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