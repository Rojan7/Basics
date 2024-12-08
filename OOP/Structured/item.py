import csv 
class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = [] 
    def __init__(self, name: str, price: int, quantity):
        assert price > 0, f"price {price} is not valid"
        assert quantity > 0, f"quantity {quantity} is not valid"


        self.__name = name
        self.__price = price
        self.quantity = quantity
        

        Item.all.append(self)
    @property
    #property decorator gives a read only attribute 
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long")
        
        self.__name = value 
    @property
    def price(self):
        return self.__price 
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def calculate_total_price(self):
        return self.__price * self.quantity
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
    @property
    def read_only_name(self):

        return "AAA"
    def __connect (self,smtp_server):
        pass
    def __send (self):
        pass

    def send_Email (self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
    def __prepare_body (self):
        return f""" 
        Hello {self.name}
        We have {self.quantity}  left in stock 
        Regards Rojan
        """
    

# Item.instantiate_from_csv()  

# print (Item.all)
print (Item.is_integer(7.1))





# for item in Item.all:
#     print (item.name)


 
# print (Item.all)