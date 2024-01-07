class Vehicles:
    sheets = 4
    doors = 2

    def __init__(self, brand, colour):
        self.t1 = brand
        self.t2 = colour

    def brand(self):
        print("This is ", self.t1, " and ", self.t2, " colour,", wheels, "wheels,", self.sheets, "sheets.")


wheels = 3

v1 = Vehicles('bmw', 'white')
v2 = Vehicles('ferrari', 'red')


v1.brand()
v2.brand()
