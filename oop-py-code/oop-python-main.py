# Object Oriented Programming

'''
def hello():
	print("hello")

x = 1
print(type(hello))
'''

'''
string = "hello"
print(string.upper())
'''

#creating class
class Dog:

	#special method init
	def __init__(self, name, age):
		self.name = name #Attribute of the class Dog - unique for every object
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age


	def add_one(self, x):
		return x + 1

	def bark(self):
		print("bark")


d = Dog("Tim", 34)
print(d.get_name())
d.set_age(22)
print(d.get_age())

d2 = Dog("Bill", 12)
print(d2.get_name())
print(d2.get_age())

d.bark()

print(d.add_one(5))
print(type(d))

