#decorators getters and setters

class Student:
    def __init__(self, name, age): #konstruktori i klases e cila eshte pjesa qe behet run e para
        self.__name=name #ketu deklarohen te gjitha atributet e klases
        self.__age==age
    #deklarimi i metodes get
    @property
    def name(self):
        return self.__name

    #deklarimi i metodes set
    @name.setter
    def name(self,name):
        self.__name=name
