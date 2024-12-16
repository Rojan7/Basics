import random

def computer_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    max_guess = 5

    while count < max_guess:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        count += 1
        
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly!")
            return  # Exit the function when guessed correctly
        
        print(f"Attempts left: {max_guess - count}")
    
    # If the loop ends without a correct guess
    print("You lost! Better luck next time.")
    
# Test the function
computer_guess(10)
