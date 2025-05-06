

contact_info={
    "alice":{
        "phone":"045345922",
        "email":"alice@gmail.com",
        "address":"rruga kryeziu",
        "birthday":"30/04/2010",
    },
    "bob":{
        "phone":"045356922",
        "email":"bob@gmail.com",
        "address":"rruga londra",
        "birthday":"30/04/2010",
    },
    "eve":{
        "phone":"045306522",
        "email":"eve@gmail.com",
        "address":"rruga pylli",
        "birthday":"30/04/2010",
    }
}
print(contact_info)

#1. print bob info
#2. create two new personas
#3. print new personas info
#4. update new personas number


bob_info=contact_info["bob"]
print(bob_info)

contact_info["erin"]={
        "phone":"045927357",
        "email":"kingi@gmail.com",
        "address":"rruga kingi",
        "birthday":"30/04/2010",}
print(contact_info["erin"])

contact_info["baba"]={
        "phone":"045927357",
        "email":"baba@gmail.com",
        "address":"rruga baba",
        "birthday":"30/04/2010",}
print(contact_info["baba"])

contact_info["erin"]["phone"]="044274667"
print(contact_info["erin"]["phone"])


