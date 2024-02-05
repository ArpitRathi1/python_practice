# Ques) Given a string and a number N, we need to mirror the characters from the n-th position upto the length of the string in alphabatical order.
# In mirror operation, we change "a" to "z","b" to "y",and so on.

input_string=input("Enter string:")
n=int(input("Enter n:"))

# Creating dict for mirror operation.
alpha="abcdefghijklmnopqrstuvwxyz"
alpha_rev=alpha[::-1] # To reverse alpha string.
dict_1=dict(zip(alpha,alpha_rev))

# Finding the part of the string on which we will perform mirror operation.
prefix=input_string[0:(n-1)]
suffix=input_string[(n-1):]

# Finding mirror string.
mirror=""
for i in range (0,len(suffix)):
	mirror=mirror + dict_1[suffix[i]]

# Creating final string.

result=prefix+mirror
print(result)