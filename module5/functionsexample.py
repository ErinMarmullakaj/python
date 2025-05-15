from email import message_from_string
from email.policy import default

total=0

for number in range(1,11):
    if number%2==0:
        total+=number
print("the sum of even numbers from 1 to 11", total)

#this is defining a function. keyword def in python defines functions
def greet():
    print("hello world")
#this is how we use the function
greet()

def greet_person(name):
    print("hello name")

greet_person("alma")

def shuma(x,y): #this type of funtion returns smth in this case a number
    z=x+y
    return z
rezultati=shuma(3,4)
print("3+4" ,rezultati)


#local variable - variabla vetem brenda funksionit
def greet(name):
    message=f"hello, {name}!"
    print(message)
greet("alma")

#print(message) - this outputs an error because the message variable is defined only for the functiobn

#argumentet dhe definimi i tyre
def greet_person(name,greeting="hello"):
    mesazhi=f"{greeting}, {name}"
    return mesazhi
default_greeting=greet_person("alma")
print(default_greeting)
costum_greeting=greet_person("alma","goodmorning")
print(costum_greeting)

pershendetje="hi"
def greet_people(name):
    global pershendetje
    return f"{pershendetje}, {name}"
variabla=greet_people("alma")
print(variabla)





