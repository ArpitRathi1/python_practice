from expresion import *
from tech_stack import *
from postfix import *
from solution import *

Expression_1 = Expression()
expression = Expression_1.split_str()
postfix_ex=postfix(expression)
print(solution(postfix_ex))