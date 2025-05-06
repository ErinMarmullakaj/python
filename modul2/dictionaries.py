#collection of items ordered mutable not indexable, works on a pair key:value

contact_info={
    "alma":"049992345",
    "erin":"049654321"
}
print(contact_info)
alma_info=contact_info["alma"]
print(alma_info)
contact_info["Orkidea"]="045987654"
contact_info["orkidea"]="045987654"
del contact_info["orkidea"]
print(contact_info)
keys=contact_info.keys()
print(keys)
values=contact_info.values()
print(values)
items=contact_info.items()
print(items) #print out the key value pair as lists



