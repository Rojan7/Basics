#12)WAP to find the sum of all items in a dictionary
dict = {'a': 100, 'b':200, 'c':300}
dict_2 = {'x': 25, 'y':18, 'z':45}

sum = 0
for items in dict:
    sum = sum + dict[items]
print (sum)
sum = 0
for items in dict_2:
    sum = sum + dict_2[items]
print (sum)