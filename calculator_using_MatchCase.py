# Ques) Write a python program to create a calcultor using match case.

num1=float(input("Enter number one:"))
num2=float(input("Enter number two:"))

operator=input("Enter operator:")

match operator:
	case "+":
		print("Sum is",num1+num2)
	case "-":
		print("Difference is",num1-num2)
	case "*":
		print("Product is",num1*num2)
	case "/":
		print("Quotient is",num1/num2)
	case "%":
		print("Remainder is",num1%num2)
	case "**":
		print("Result is",num1**num2)
	case "//":
		print("Floor division is",num1//num2)
	case _:
		print("Invalid operator")