# Ques) Write a python program to seprate character and numeric values from the given list and store it in a seprate list:
# l1=[1,2,"A","C","F",7,5,"P",3]

l1=[1,2,"A","C","F",7,5,"P",3]
digit=[]
character=[]
for  i in l1:
	if str(i).isdigit():
		digit.append(i)
	else:
		character.append(i)
print("Digits in this list : ",digit)
print("Character in this list : ",character)