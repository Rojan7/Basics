class Sum :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2    
    def sum(self):
        return self.num1 + self.num2
num1 = int(input ("enter first number"))
num2 = int(input ("enter second number"))
obj = Sum(num1,num2)
print (obj.sum())    

