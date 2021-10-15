class main(object):
	
	def __init__(self, x, y):
		self.x, self.y = x,y
	
	def __repr__(self):
		return 'Output: {} {}'.format(self.x,self.y)
	
	def __str__(self):
		return 'Output: {} {}'.format(self.x,self.y)
		
z = main(1,"Noob")
print(z.__str__())
