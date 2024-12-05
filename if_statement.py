# temperature = int(input ("enter the temperature"))

# if temperature > int(30):
#     print ("it is hot outside")
# elif temperature < int(0):
#         print ("it is freezing cold outside")
# elif temperature <10 and temperature >0 :
#         print ("it is cold outside very verycold")
# else:
#         print ("it is neither hot nor cold")


# kgs to pounds
Weight1 = input("enter the weight ")
Weight = int(Weight1)
Decision = input ("is it in kgs or in pounds  (k/l??")
if Decision == "k" or Decision == "K":
     print (Weight * 2.2046)
elif Decision == "l" or Decision == "L":
     print (Weight / 2.2046)
else:
     print ("invalid input")