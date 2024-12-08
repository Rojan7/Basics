# item1 = 'phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print (type(item1_price_total))

# <class 'str'>
# <class 'int'>
# <class 'int'>
# <class 'int'> the thing is every data type has a class associated with it so creating our own datatype can be done by creating a class
#this will create a chain for learning object oriented programming
class Item:
    def __init__(self,name :str,price:int ,quantity):#all these parameters must be mandtorily passed to the constructor but if wee have to make some attributes
                                            #optional then we can make them optional by passing a zero or default value
        # print(f"hello I am a constructor and I am created successfully for {name}")
        assert price >0 , f"price {price} is not valid"
        assert quantity >0 , f"quantity {quantity} is not valid"


        self.name = name
        self.price = price
        self.quantity = quantity 
        total = self.price * self.quantity
        print(total)

    # def calculate_total_price(self, quantity, price): 
    #     print(quantity * price) 
    



item1 = Item("phone",100,-3)
# item1.calculate_total_price(item1.quantity,item1.price)
#



item2 = Item("laptop",1000,3)
# item2.calculate_total_price(item2.quantity,item2.price)
#

print(item1.name)
print(item2.name)




