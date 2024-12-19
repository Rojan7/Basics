# Wap to check weather a given number is odd or even
number = input("Enter a number")


def check_evenORodd(num):

    if num % 2 == 0:

        return 1
    else:
       return 0


result = check_evenORodd(int(number))

if result == 1 :
    print("even")
else :
    print("odd")
