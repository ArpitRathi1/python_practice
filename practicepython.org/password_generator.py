# Ques) Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
# Extra:
# 1) Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import random

def weak_password():
	char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	weak_password="".join(random.sample(char,8))
	return weak_password

def strong_password():
	char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#!$%^&*+?"
	strong_password="".join(random.sample(char,8))
	return strong_password

user_choice=int(input("Welcome to my password generator\nPress 1 to generate a weak password\nPress 2 to generate a strong password : "))
if user_choice==1:
	output=weak_password()
	print(output)
elif user_choice==2:
	output=strong_password()
	print(output)
else:
	print("Invalid number")