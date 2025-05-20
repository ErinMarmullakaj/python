age=25
age_As_string=str(age)
print(age_As_string, "of type ", type(age_As_string))

print(bool(0)) #this is false because 0 is false in boolean
print(bool(42)) #this is true because 42 transaltes as 1

print(bool(""))
print(bool("hello"))


#implicit type casting
x=32
y=5.3
rezultati=x+y
print(rezultati, " of type ", type(rezultati))

a=5
b="3"
rezultati=a*int(b)
print(rezultati, " of type ", type(rezultati))

c=4
rezultati2="hello"*c

#get two numbers from user input and sum them up
nr1=int(input("first number:"))
nr2=int(input("second number:"))
rezultati3=nr1+nr2
print(rezultati3)
