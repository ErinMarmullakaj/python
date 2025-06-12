lines=["hello world!\n", "welcome to python\n"]
with open("example.txt","w") as file: # we open the file with premissions to write
    file.writelines(lines) # we write on multiple lines

print("hello")