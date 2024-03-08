# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old . Don’t explicitly write out the year. Use the built-in Python datetime library to make the code you write work during every year, not just the one we are currently in.

import datetime

now=datetime.datetime.now()
current_year=now.year 
name=input("Enter your name : ")
age=int(input("Enter your age : "))
year_100=current_year-age+100
print(f"Hii {name},you will be 100 years old in the year {year_100}")