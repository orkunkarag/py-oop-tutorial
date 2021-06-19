#Static Methods

class Math:

	@staticmethod #static method
	def add5(x):
		return x + 5

	@staticmethod #static method
	def add10(x):
		return x + 10

	@staticmethod
	def pr():
		print("run")


Math.pr()

print(Math.add5(5))

