class Computer:
    def config(self):
        print("Hello world")


com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.__eq__(com2, com1)
com1.config()


