names=["alma", "blerta","dhurata","shpati",]
for names in names:
    print(name)

#shembulli 2
sentence_shembulli="hello, world5"
for char in sentence_shembulli:
    if char.isalpha(): #kthen true od false if char is a letter
        print(char)


#shembulli 3 me rage function
for numri in range(1,6): #range(x,y) x ku fillon dhe y ku mbaron mirpo nuk e perfshin y
    print(numri)

#find max in a list
numrat=[33,44,55,66,77,88,99,100]
max=numrat[0]
for num in numrat:
    max=num
print("the max value of the list is ", max)