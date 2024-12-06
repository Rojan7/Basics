# # # # # def get_greeting_name (name) :
# # # # #     return f"hello {name}"

# # # # # message = get_greeting_name("rojan")
# # # # # print (message)
# # # # #all python functions return none by default


# # # # def sum (num1,num2):
# # # #     return num1 + num2

# # # # number1 = float(input ("enter first number"))
# # # # number2 = float (input ("enter second number"))
# # # # result = sum (number1,number2)
# # # # print (result)

# # # def increment (num,by) :
# # #     return num + by

# # # number = int(input ("enter number"))
# # # by = int (input ("enter  by how much you want to increase the particular number"))

# # # result = increment (number,by)
# # # print ("when "+str(number)+"is increased by "+str(by)+"the result is",result)

# # def increment (number,by=1): #all the optional parametes are placed at last of all the other oparameters
# #     return number + by
# # result = increment (2)
# # print (result)
# def multiply (*numbers):
#     Total = 1
#     for number in numbers:
#         Total = Total * number
#     return Total
# print (multiply(1,2,3,4,5))
def save_user (**user): # this now acts as a dictionary which has a key value pair 
    print (user)
    print (user ["id"])

save_user (id=1,name="rojan",age=20,is_active=True)