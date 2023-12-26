marks=int(input("Enter the marks obtained by student:"))

if marks>100:
	print("Invalid marks")
elif marks>80:
	print("A grade")
elif marks>60:
	print("B grade")
elif marks>40:
	print("C grade")
else:
	print("F grade")