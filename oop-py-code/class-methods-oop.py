#Class Methods

class Person:

	number_of_people = 0 #class attribute

	def __init__(self, name):
		self.name = name
		Person.add_person()

	@classmethod #class Method
	def number_of_people_(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1


p1 = Person("tim")
p2 = Person("jill")

print(Person.number_of_people_())

