# Write a program to find vowels in a list.

lst=["A","a","b","r","E","G","i","x","d"]
string="aeiou"
vowels=[]
for i in lst:
	if i in string:
		vowels.append(i)
print(vowels)