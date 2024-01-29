ages=(10,30,15,17,65,11,9)

list=[]

# Adding values in a list.
for i in reversed(ages):
	list.append(i)

# Typecasing list into tuple.
Output_tuple=tuple(list)

# Printing output_tuple.
print(Output_tuple)