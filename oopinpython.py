class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi,This is ", self.name)


p1 = Person('Sudheera')
p2 = Person('Wishmi')
Person.say_hi(p1)
p1.say_hi()
p2.say_hi()
