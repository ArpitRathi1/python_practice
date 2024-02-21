# Properties of tuple-
# 1) Indexed.
# 2) Ordered.
# 3) Immutable.
# 4) Duplicates are allowed.
# 5) Tuple can be of any data type.

# Creating a tuple.
fruits=("Mango","apple","kiwi")
fruits_1=("guava","orange")

# Creating tuple with one item-you should add a , and the end.
fruit=("guava",)
fruit_1=tuple("banana")

# Check type.
print(type(fruits))
print(type(fruit))
print(type(fruit_1))

# Check length of tuple.
print(len(fruits))

# Accessing items in the tuple.
print(fruits[2])     # positive indexing
print(fruits[-1])    # negative indexing
print(fruits[1:3])   # range indexing
print(fruits[-2:])   # negative range indexing

# Traverse a tuple
for i in fruits:
	print(i)

# Concatenate two tuples.
fruits=fruits+fruits_1
print(fruits)

# Unpacking a tuple.
fruit1,fruit2,fruit3,fruit4,fruit5=fruits
print(fruit1)
print(fruit2)
