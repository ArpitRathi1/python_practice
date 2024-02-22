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

# Joining two sets.
s2={1,2,3}
s3={5,6,1}

"""s2.update(s3)             # update function will add items of s3 in s2.
print(s2)

s4={10,11,12}
s5={15,11,18}

s6=s5.union(s4)           # union function will add items of s5 and s4 in a third variable s6.
print(s6) """


# To keep only duplicates while joining.

"""s2.intersection_update(s3)
print(s1)"""

# To keep all values except duplicates.

"""s2.symmetric_difference_update(s3)
print(s1)"""
