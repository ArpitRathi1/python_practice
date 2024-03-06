# Ques) Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old using f-strings instead of the + operator to print the resulting output message.
# Solution-

name=input("Enter your name : ")
age=int(input("Enter is your age : "))
year_100=2024-age+100
print(f"Hii {name},you will be 100 years old in the year {year_100}")
