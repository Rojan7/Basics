#Write a Python program to create a person class. Include attributes like name, country and date of
#birth. Implement a method to determine the person's age.

class Person :
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def age(self):
        return 2024 - self.date_of_birth

def get_user_input():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    date_of_birth = int(input("Enter your date of birth: "))
    return Person(name,country,date_of_birth)

person = get_user_input()
print (f"{person.name} is from {person.country} and is {person.age()} years old")