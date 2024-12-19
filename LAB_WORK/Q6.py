#6)WAP to calculate the factorial of an input number.
#used a recursive function for this purpose
def calculate_fact(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else :
        return num *calculate_fact(num-1)

get_num = int(input("enter a number"))
fact = calculate_fact(get_num)
print(fact)
   
        