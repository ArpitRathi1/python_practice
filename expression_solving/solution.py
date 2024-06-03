from expresion import *
from tech_stack import *
from postfix import postfix

def solution(postfix_ex):
	solution_stack = tech_stack()
	operator_priority = {"+":1,"-":1,"*":2,"/":2}
	for i in postfix_ex:
		if i not in operator_priority:
			solution_stack.push(i)
		else:
			value_1 = float(solution_stack.pop())
			value_2 = float(solution_stack.pop())
			if i == "+":
				result = value_2 + value_1
				solution_stack.push(result)
			elif i == "-":
				result = value_2 - value_1
				solution_stack.push(result)
			elif i == "*":
				result = value_2 * value_1
				solution_stack.push(result)