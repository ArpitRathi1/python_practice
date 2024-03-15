def string_check(string):
	for i in string:
		if i.isalpha() or i.isspace():
			return True
		else:
			return False