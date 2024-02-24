st_1="new york"
# upper()-to convert characters of the string to upper-case.
st_2=st_1.upper()
print(st_2)

# lower()-to convert characters of the string to lower-case.
st_3=st_2.lower()
print(st_3)

# Note-upper() and lower will ignore other characters apart from alphabates.
s="abc123"
s1=s.upper()
print(s1)

# capitalize()- To capitalize first character of string.
st_4=st_1.capitalize()
print(st_4)

# strip()- for stripping/removing any trailing whitespaces.
st_5="    hello world   "
print(st_5.strip())
print(st_5)          # strip() will not change anything in original string.

# replace()- replace old_substring with new_substring count number of times.
# syntex- string.replace(old_substring , new_substring , count)
st_6="hello world, what a beautiful world this is!!"
# If you want to change Arpit with Ashwin.
st_7=st_6.replace("world","earth")    # if count was not given all occerance of old_string will be replaced.
print(st_7)
st_8=st_6.replace("world","earth",1)  # if count was given it will replace only count number of old_strings.
print(st_8)

# spilt()-used to split the string into a list of substring.
# syntax-string.split(sep,maxsplit)
st_9="Apple Banana Cherry Guava"
l1=st_9.split()                  # By default seprator is white space.
print(l1)
st_10="Arpit,Ashwin,Ankit"
l2=st_10.split(",")
print(l2)
l3=st_10.split(",",1)
print(l3)

# Concatination-
st_11="Hello,"
st_12="I am Arpit."
st_13=st_11+st_12
print(st_13)

# String formating.
name="Arpit"
marks=90
st_14="I am {n} and i got {m} marks in maths.".format(n=name,m=marks)
print(st_14)
