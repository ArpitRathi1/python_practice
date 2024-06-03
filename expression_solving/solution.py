from expresion import *
from tech_stack import *
from postfix import postfix

def solution(postfix_ex):
	solution_stack = tech_stack()
	operator_priority = {"+":1,"-":1,"*":2,"/":2}
	for i in postfix_ex:
		if i not in operator_priority:
			solution_stack.push(i)