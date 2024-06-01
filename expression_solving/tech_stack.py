class tech_stack : 
	def __init__(self):
		self.body = []
		self.top = -1

	def push(self,item):
		self.body.append(item)
		self.top +=1