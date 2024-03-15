from utils import *


user_choice=True
while user_choice==True:
	choice = int(input("Welcome to Our Marks Management System \nPress 1 : To Add New Marks Entry \nPress 2 : Show all Entries\nPress 3 : Generate Results\nPress 4 : Show Results and Grade\nEnter Your Choice : "))
	if choice == 1 :
		add_entry()
	elif choice == 2 :
		show()
	elif choice == 3:
		generate_result()
	elif choice == 4 :
		show_results()
	else : 
		print("Invalid Choice")
	choice_1=input("Press Y to run this program again or any key to exit : ")
	if choice_1.lower()=="y":
		user_choice=True
	else:
		user_choice=False
		print("Exiting the program.")