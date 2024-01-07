class Country:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def show(self):
        print(self.name, "speaks", self.language)

    class President:
        def __init__(self, pname, wife):
            self.pname = pname
            self.wife = wife

        def show(self):
            print("The president is", self.pname, "and wife is", self.wife)


c1 = Country('USA', 'English.')
c2 = Country('Sri lanka', 'Sinhalese.')

c1.show()
c2.show()
# inner class, object created inside outer class
p1 = c1.President('Trump', 'Melania')
p2 = c2.President('Rajapaksha', 'Shiranthi')

p1.show()
p2.show()
# object of inner class created outside of outer class
pres1 = Country.President('Sunak', 'Rithika')
pres1.show()
