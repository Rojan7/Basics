name = "Rojan Adhikari"
print (name.upper())
print (name.lower())
print (name.title())
print (name.find("Adhikari"))
print (name.replace("Adhikari", "Adhikaaari"))
print (name.find("R"))
print (name.find("z"))
print(name) #this proves that all the changes are not permanent that means all the functions we played with did not actually changed our original strings by any bits
print ("Rojan" in name) # this checks weather a string is present in another string or not

if "Rojan" in name:
    print ("present")
else:
    print ("not present")