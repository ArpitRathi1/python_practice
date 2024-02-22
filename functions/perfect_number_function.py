def perfect_number(num):
	if num<0:
		return False
	else:
		sum_of_divisor=0
		for i in range(1,num):
			if num%i==0:
				sum_of_divisor=sum_of_divisor+i
	if num==sum_of_divisor:
		return True	
	else:	
		return False			