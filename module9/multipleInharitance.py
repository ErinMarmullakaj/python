class Vertebrate()
    def __init__(self, backBone=True):
        self.has_Backbone=backBone
    def vertebrate_info(self):
        print("vertebrates have a backbone")

class Aquatic
    def __init__(self, habitat="water"):
        self.habitat=habitat
    def aquatic_info(self):
        print("aquatic animals live under water ")

class Fish(Vertebrate,Aquatic):
    def __init__(self, species, backBone=True, habitat="water"):
        super().__init__(backBone=backBone)
        self.species=species
        self.habitat=habitat
    def fish_info(self):
        print(f"the {self.species} is a type of fish found ")
    def swim(self):
        print("the fish is swimming ")
        
goldfish=Fish("goldfish")
print(goldfish.has_Backbone)
print(goldfish.habitat)
goldfish.vertebrate_info()