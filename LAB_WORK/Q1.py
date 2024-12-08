#Wap to check weather a given number is odd or even
number = input("Enter a number")


def check_evenORodd (num) :
 
    if num % 2==0 :

        print (str(num)+ " is even")
    else :
     print (f"{num} is odd")

 

check_evenORodd(int(number))
    
