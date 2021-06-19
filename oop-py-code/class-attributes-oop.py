#Class Attributes - attributes attached to classes that don't change from obj to obj

class Person:

	number_of_people = 0 #class attribute

	def __init__(self, name):
		self.name = name
		Person.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")

print(p2.number_of_people)

