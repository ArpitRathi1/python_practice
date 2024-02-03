# Properties of dictionary-
# 1) Unindexed.
# 2) Ordered.
# 3) Changable.
# 4) Duplicates not allowed-
# a) Duplicate keys not allowed.
# b) Values can be duplicate.
# 5) Items can be of any datatype.

# Creating a dictionary.
roll_no={
	"Arpit":1,
	"Ankit":2,
	"Ashwin":3	
}
roll_no_2={
	"Sumit":6,
	"Adi":7
}
print(roll_no)                  # Printing dict.
print(len(roll_no))             # Checking length of dict.
print(type(roll_no))            # Checking type.

# Accessing value in dict.
print(roll_no["Arpit"])         # If key not found in dict it will give key error.
print(roll_no.get("Arpit"))     # If key not found in dict it will not give any error.
print(roll_no.keys())           # To access all keys.
print(roll_no.values())         # To access all values.

# To update an existing item.
roll_no["Arpit"]=4              
print(roll_no)
# To add new item.
roll_no["Prakhar"]=5
print(roll_no)

# Add another dict.
roll_no.update(roll_no_2)
print(roll_no)

# To remove items.
roll_no.pop("Adi")              # To remove any specific item.   
print(roll_no)                  
roll_no.popitem()               # To remove last item
print(roll_no)
# roll_no.clear()               # To empty the dict.
# print(roll_no)
# del roll_no                   # To delete entire dict.
# print(roll_no)

# Loop through a dict.
for i in roll_no:           # To print all keys.
	print(i)
for i in roll_no:           # To print all values.
	print(roll_no[i])
for i in roll_no.items():   # To print both keys and values.       
	print(i)

# Creating a dictionary using fromkeys() function.
lst=["Adi","Sumit","Gopi","Shubham"]
value=0
dic=dict.fromkeys(lst,value)
print(dic)

# Creating a dictionary using zip function.
l1=["Sia","Jia","Tia"]
l2=[1,2,3]
dic_1=dict(zip(l1,l2))
print(dic_1)