# Properties of set-
# 1) Unindexed.
# 2) Unordered.
# 3) Immutable-Can't update existing values,but you can remove or add new element.
# 4) Duplicate value not allowed.
# 5) Any datatype or mix of different data type.

# Creating a set.
s1={"Arpit","Ankit","John","Adi"}
print(s1)                 # Printing set (Sets are unordered)
print(type(s1))           # Checking type
print(len(s1))            # Checking lenth of set

# Accessing items of a set.
for i in s1:
	print(i)

# Adding element in a set.
s1.add("Ashwin")
print(s1)

# Adding another sequence.
l1=["Prakhar","Sumit"]
s1.update(l1)
print(s1)

# Removing items.
s1.remove("Adi")
print(s1)                 # If item is not present in the set then remove function will throw an error.
s1.discard("Adi")
print(s1)                 # If item is not present in the set then discard function will not throw an error.
