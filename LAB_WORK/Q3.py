#3)WAP to calculate sum, diff, product and quotient between two input numbers using a single function.

def calculate (num1,num2) :
    print ("sum = " +str(num1+num2))
    print ("diff = " +str(num1-num2))
    print ("prod = " +str(num1*num2))
    print ("quotient = " +str(num1//num2))



num1 = float(input ("enter 1st number"))
num2 = float( input ("enter 2nd number"))
calculate (num1,num2)