from item import Item
class Phone(Item):
    
    def __init__(self, name: str, price: int, quantity,broken_phones=0):
      #super function incoming
      super().__init__(name, price, quantity)
      assert broken_phones >= 0, f"broken_phones {broken_phones} is not valid"

      self.broken_phones = broken_phones