#9)WAP program to sum all the items in a list.

def sum_of_lists(list1):
    sum =0
    for items in range(0,len(list1),1):
        sum = sum + int(list1[items])
    print (sum)
    pass

list1 = [1,2,3,4,5,6]

sum_of_lists(list1)
