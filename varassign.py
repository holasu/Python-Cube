class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def who_id(self):
        print("This is ", self.name, " and, I'm ", self.colour)


a1 = Animal('Girrafe', 'brown')
a2 = Animal('Zibra', 'black & white')

a1.who_id()
a2.who_id()

