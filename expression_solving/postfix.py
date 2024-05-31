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

		elif i not in operator_priority:
			post_stack.push(i)
		
		elif i in operator_priority:
			L = temp_stack.length()
			if L == 0 :
				temp_stack.push(i)
			else:
				j = temp_stack.top_value()
				if operator_priority[i] > operator_priority[j]:
					temp_stack.push(i)
				else : 
					while operator_priority[i] <= operator_priority[j] :
						item_opt = temp_stack.pop()
						post_stack.push(item_opt)
						if temp_stack.length() == 0:
							break
						else : 
							j = temp_stack.top_value()
					temp_stack.push(i)
	else : 
		x = temp_stack.length()
		for i in range(x):
			item_opt = temp_stack.pop()
			post_stack.push(item_opt)

	return post_stack.show()