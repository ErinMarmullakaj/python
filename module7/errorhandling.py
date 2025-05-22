#error handling try, except, finally
#try- writing of the needed code
#except - what happens if an error happens in the try part
#finally- part of code that is always run

#this is dedicated for errors that programmers do not predict

try:
    rezultati=10/0
    nr1=int(input("shkruani nr1:"))
    nr2=int(input("shkruani nr2:"))
    rezultati=nr1/nr2
    print("rezultati:" , rezultati)
except ZeroDivisionError:
    print("ke gabu per arsye qe je duke pjestu me 0")

#second example

fruits={
    "apples":5,
    "banana":6,
    "orange":7,
}
try:
    print(fruits["cherry"])
except KeyError:
    print("the key does not exist in the dictionary")

#third example
try:
    try_to_int=int(text)
except Exception as e:
    print("an error occured while parsing the data:" e)

try:
    rezultati=10/2
except ZeroDivisionError:
    print("division by zero error occured")
else:
    print("division succesful, result:" , rezultati)

#fifth example
try:
    rezultati=10/0
except ZeroDivisionError:
    print("division by zero error occured ")
finally:
    print("this part of code always runs ")