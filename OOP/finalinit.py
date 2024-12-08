import csv
class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = [] 
    def __init__(self, name: str, price: int, quantity):
        assert price > 0, f"price {price} is not valid"
        assert quantity > 0, f"quantity {quantity} is not valid"


        self.name = name
        self.price = price
        self.quantity = quantity
        

        Item.all.append(self)
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    def calculate_total_price(self):
        return self.price * self.quantity
    @classmethod # this is a decoraator 
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f: # this is a context manager that opens the file
            reader = csv.DictReader(f) # this is a dictionary reader
            items = list(reader)# this is a list of dictionaries 
            for item in items:
              Item(
                name = item.get('name'),
                price = float( item.get('price')),
                quantity = int (item.get('quantity'))
              )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int) 

      
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self. price},{self.quantity})"

# Item.instantiate_from_csv()  

# print (Item.all)
print (Item.is_integer(7.1))





# for item in Item.all:
#     print (item.name)


 
# print (Item.all)
class Phone(Item):
    
    def __init__(self, name: str, price: int, quantity,broken_phones=0):
      #super function incoming
      super().__init__(name, price, quantity)
      assert broken_phones >= 0, f"broken_phones {broken_phones} is not valid"

      self.broken_phones = broken_phones

      
   
 
phone1 = Phone("jscPhonev10",500,5,1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20",700,5,1)
print(Item.all)
print(Phone.all)

