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

def check_grade(x):
	"""This function is created to give grades to students according to their performance in internal examination."""
	if x<=40 and x>=35 :
		return("A")
	elif x<=34 and x>=30 :
		return("B")
	elif x<=29 and x>=25 :
		return ("C")
	elif x<=24 and x>=20 :
		return("D")
	else : 
		return("Fail")

def generate_result():
	"""This function is created to generate result and the result is gererated by picking up two best scores of a student out
	of three."""
	f1 = open("internal_marks.txt", "r")
	every_entry = f1.readlines()
	f1.close()
	f1 = open("results.txt", "w")
	for i in every_entry:
		i = i.replace("\n", "")
		elements = i.split(",")
		x = int(elements[1])
		y = int(elements[2])
		z = int(elements[3])
		if x<=y and x<=z:
			lowest_score = x
		elif y<=x and y<=z:
			lowest_score = y
		else:
			lowest_score = z
		total = (x+y+z)
		final_marks = total-lowest_score
		grade = check_grade(final_marks)
		result_entry = "{},{},{},{},{},{}\n".format(elements[0], elements[1], elements[2], elements[3], final_marks,grade)
		f1.write(result_entry)
	f1.close()

def show_results():
	"""This function is created to show result and grade obtained by students"""
	f1 = open("results.txt", "r")
	entry = f1.readlines()
	f1.close()
	for i in entry:
		i = i.replace("\n", "")
		elements = i.split(",")
		print("-------------------------")
		print("Name of student : ", elements[0])