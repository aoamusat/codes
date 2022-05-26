class A:
	initialized = True
	numberOfObj = 0

	def __init__(self, a):
		if self.initialized:
			self.initialized = False
		self.numberOfObj += 1
		self.a = a
	
	def addPseudoObj(cls):
		cls.numberOfObj += 1
		
a = A(7)
a.addPseudoObj()
print(a.initialized, a.numberOfObj)
aa = A(1)
print(aa.numberOfObj)
