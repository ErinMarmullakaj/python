class Animal:
    def __init__(self,name): #shembulli per ni konstruktor dhe nje variable e cila po iniciohet per ket klas
        self.name=name

    def sound(self):
        print("generic animal sound")
    def description(self):
        print(f"this is an animal named {self.name}")


class Dog(Animal):
    def __init__(self, breed, name): #konstruktori
        self.breed=breed #variabla qe vlen vetem per ket klas
        super().__init__(name) # ketu thirret konstruktori i superklases

    def sound(self):
        print("woof! woof!")

    def description(self):
        super().description()
        print(f"breed {self.breed}")


class Cat(Animal):
    def __init__(self, color, name):
        self.color=color
        super().__init__(name)

    def sound(self):
        print("mjau! maju!")

    def description(self):
        super().description()
        print(f"color {self.color}")

rex=Dog("malonois", "rex")
rex.sound()
rex.description()

garfield=Cat("violet","garfield")
garfield.sound()
garfield.description()




