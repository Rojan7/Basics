
from item import Item


item1 = Item("my item", 100, 3)
# item1.name = "other Item" this will not work because we have treated it like a private class!!
print (item1.name)
item1.name = "other item"

# item1.read_only_name = "AAA" we cannot set a property unless we use a setter 

item1.send_Email()
print(item1.read_only_name)
print(item1.name)