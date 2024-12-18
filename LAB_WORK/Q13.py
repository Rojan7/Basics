#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def convert(string):
    new_string = ""
    for character in string :
        if character.islower():
            new_string += character.upper()
        else:
            new_string += character.lower()
    return new_string
take_string = input("Enter a string")
print(convert(take_string))
 