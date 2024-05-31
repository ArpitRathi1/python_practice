from expresion import *
from tech_stack import *

def postfix(expresion):
	operator_priority = {"+":1,"-":1,"*":2,"/":2,"(":0,}
	temp_stack = tech_stack()
	post_stack = tech_stack()