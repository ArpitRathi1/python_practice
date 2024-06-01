class tech_stack : 
	def __init__(self):
		self.body = []
		self.top = -1

	def push(self,item):
		self.body.append(item)
		self.top +=1

	def pop(self):
		if self.top == -1 :
			return None
		else : 
			self.top-=1
			return self.body.pop()

	def show(self):
		return self.body

	def length(self):
		return len(self.body)