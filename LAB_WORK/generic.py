from itertools import permutations

def solve_cryptarithm(equation):
   
    unique_chars = set(filter(str.isalpha, equation))
    if len(unique_chars) > 10:
        raise ValueError("besi unique character not supporteddd")

    
    left_side, right_side = equation.split("==") # split the equation into left side and right side
    left_terms = left_side.split("+") # split the left side into terms
    left_terms = [term.strip() for term in left_terms] # remove leading/trailing whitespace
    right_side = right_side.strip() # remove leading/trailing whitespace

    
    for perm in permutations(range(10), len(unique_chars)):#unique term ko total permutation nikalera tesma iterate garne
        char_to_digit = dict(zip(unique_chars, perm))#hashmap create garne unique character ra perm ko

        
        if any(char_to_digit[each_term[0]] == 0 for each_term in left_terms + [right_side]):#if leading zero is present
            continue

        
        try:
            left_values = [
                #left side ko each term ko each character ko tyo hashmap ma sabai character ma assigned key athawa number lai string ma rakhera integer banaune
                int("".join(str(char_to_digit[char]) for char in term))for term in left_terms
                
            ]
            right_value = int("".join(str(char_to_digit[char]) for char in right_side))
        except KeyError:#if unique character is not present missing types
            continue

        
        if sum(left_values) == right_value:
            
            solution = " + ".join(str(value) for value in left_values)
            return f"{equation} is satisfied by: {solution} = {right_value}"

    return "No solution found."


equation = "TWO + TWO == FOUR"
print(solve_cryptarithm(equation))
