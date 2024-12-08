class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    def __init__(self, name: str, price: int, quantity):
        assert price > 0, f"price {price} is not valid"
        assert quantity > 0, f"quantity {quantity} is not valid"

        self.name = name
        self.price = price
        self.quantity = quantity
        total = self.price * self.quantity
        print(total)
    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("phone", 100, 3)



item2 = Item("laptop", 1000, 3)


print(Item.pay_rate)
print(item1.pay_rate) 
print(item2.pay_rate)# this means that payrate can be accessed from class level and also instance level

print (item1.__dict__)#provides all the attributes of the object in dictionary
print (Item.__dict__)#provides all the attributes of the class

item1.apply_discount()
print (item1.price)

#now let's say there is a case that I shall put a differeent discunt rate to laptop this can be done by
item2.pay_rate = 0.7
item2.apply_discount()
print (item2.price)
 
