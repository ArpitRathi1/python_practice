def string_check(string):
	for i in string:
		if i.isalpha() or i.isspace():
			return True
		else:
			return False

def add_entry():
	"""This function is created for addinf new enteries in internal_marks.txt file."""
	name_of_student = input("Enter Name of the Student : ")
	mark_in_internal_one = int(input("Enter marks of student in first internal examination : "))
	mark_in_internal_two = int(input("Enter marks of student in second internal examination : "))
	mark_in_internal_three = int(input("Enter marks of student in third internal examination : "))
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
	
		for i in every_entry :
		i = i.replace("\n","")
		elements = i.split(",")
		print("-------------------------")
		print("Name of student : ", elements[0])
		print("Marks in first internal examination : ", elements[1])
		print("Marks in second internal examination : ", elements[2])
		print("Marks in third internal examination : ", elements[3])
		print("-------------------------")
