class Expression:
	def __init__(self):
		self.input_str = input("Enter Expression to solve : ")
	def split_str(self):
		operator_list = ["+","-","*","/","%","(",")"]
		operator = ""
		operand = ""
		expression_list=[]
		for i in self.input_str:
			if i not in operator_list:
				operand = operand + i
			else:
				operator = operator + i
				expression_list.append(operand)
				expression_list.append(operator)
				operand = ""
				operator = ""
		else:
			expression_list.append(operand)