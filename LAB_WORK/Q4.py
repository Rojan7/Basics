#WAP to display prime numbers from 1 to 100

def check_prime (num):
    if num <= 1 :
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range (3,int (num **0.5)+1,2):
        if num % i == 0:
            return False
    return True
all = []
for i in range(1,100,1):
   
    if check_prime(i) == True:
        print(i)
        all.append(i)

if all == [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] :
    print("validated")
else:
    print ("notvalidated")


