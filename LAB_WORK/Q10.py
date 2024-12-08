#10)WAP program to get the largest number from a list.
my_list = [444,2,4,66,3,22,1,]
greatest = my_list[0]
for items in range (0,len(my_list),1):
    
    if my_list[items]>greatest:
        greatest = my_list[items]
print (greatest)
