class A:
	initialized = False
	numberOfObj = 0

	def __init__(self, a):
		if not A.initialized:
			A.initialized = True
		A.numberOfObj += 1
		self.a = a
