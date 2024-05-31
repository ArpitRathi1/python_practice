from expresion import *
from tech_stack import *

def postfix(expresion):
	operator_priority = {"+":1,"-":1,"*":2,"/":2,"(":0,}
	temp_stack = tech_stack()
	post_stack = tech_stack()
	for i in expresion:
		if i == "(":
			temp_stack.push(i)
		
		elif i == ")":
			while temp_stack.top_value() != "(":
				item = temp_stack.pop()
				post_stack.push(item)
			temp_stack.pop()