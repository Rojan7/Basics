#when to use class methods and when to use static merhods
class Item :
    @staticmethod
    def is_integer(num):
        pass
    #this does something that has a relationship with class but not something that must be unique per instance

    @classmethod
    def instantiate_from_csv(cls):
        pass
    ##this should also do something that has a relationship with class but usually those are used to manipulate different structures of data to instantiate objects, like we have done with th csv file
    
