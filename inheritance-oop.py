#Inheritance

class Pet:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):

	def __init__(self, name, age, color):
		super().__init__(name, age) #Reference to the super/bigger class = Pet()
		self.color = color

	def speak(self):
		print("meow")

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):

	def speak(self):
		print("bark")

class Fish(Pet):
	pass


p = Pet("Tim", 19)
p.show()

c = Cat("Bill", 34, "brown")
c.show()
c.speak()

d = Dog("Jill", 22)
d.show()
d.speak()

