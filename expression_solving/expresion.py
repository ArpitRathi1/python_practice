class Expression:
	def __init__(self):
		self.input_str = input("Enter Expression to solve : ")
	def split_str(self):
		operator_list = ["+","-","*","/","%","(",")"]
		operator = ""
		operand = ""
		expression_list=[]