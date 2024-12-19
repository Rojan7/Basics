#wap to create a module named "recursion" which has methods to compute the factorial of nth number and nth fibonacci using recursion
#python script called "dsa.py " and use the "recursion module" to compute factorial and nth fibonnaci term


def calculate_fact(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else :
        return num *calculate_fact(num-1)
def calculate_fibonacci(num) :
    if num ==1:
        return 1
    elif num == 2:
        return 2
    else :
        return calculate_fibonacci(num-1)+calculate_fibonacci(num-2)



   