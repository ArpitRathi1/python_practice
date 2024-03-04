# Ques) Write a program functions that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# "My name is Michele"
# Then I would see the string:
# "Michele is name My"
# shown back to me.
# Solution-

def reverse_word_order(string):
	lst=string.split()
	new_string=""
	for i in reversed(lst):
		new_string=new_string+i+" "
	return new_string


string=input("Enter your string : ")
output=reverse_word_order(string)
print(output)
