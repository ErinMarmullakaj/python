import os
if os.path.exixts("example.txt"):
    print("file exists!!!")

name= "alice"
age = 30

with open("output.txt", "w") as file:
    file.write("name:" +name+" \n")
    file.write("age:" +str(age)+ " \n")



