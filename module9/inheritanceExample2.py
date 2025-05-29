class Animal:
    def sound(self):
        print("generic animal sound")

class Dog(Animal):
    def sound(self):
        print("woof! woof!")

class Cat(Animal):
    def sound(self):
        print("mjau! maju!")

kafshe=Animal()

kafshe.sound()

rex=Dog
rex.sound()

tom=cat()
tom.sound()


