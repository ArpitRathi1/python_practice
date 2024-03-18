def string_check(string):
	for i in string:
		if i.isalpha() or i.isspace():
			return True
		else:
			return False

def add_entry():
	"""This function is created for addinf new enteries in internal_marks.txt file."""
	name_of_student = input("Enter Name of the Student : ")
	mark_in_internal_one = int(input("Enter first internal marks of the Student : "))
	mark_in_internal_two = int(input("Enter second internal marks of the Student : "))
	mark_in_internal_three = int(input("Enter third internal marks of the Student : "))
	if mark_in_internal_one>20 or mark_in_internal_two>20 or mark_in_internal_three>20 :
		print("Invalid Enter")
	else:
		if string_check(name_of_student):
			f1 = open("internal_marks.txt","a")
			entry = "{},{},{},{}\n".format(name_of_student,mark_in_internal_one,mark_in_internal_two,mark_in_internal_three)
			f1.write(entry)
			f1.close()
			print("Student Marks were added Successfully")
		else:
			print("Invalid Enter")

def show_entries():
	"""This function is created to show all the entries of marks obtained by students."""
	f1 = open("internal_marks.txt", "r")
	every_entry = f1.readlines()
	f1.close()
