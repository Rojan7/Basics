import random
def play() :
    user = input("'r' for rock 'p' for papers and 's' for scissors").lower()
    computer = random.SystemRandom().choice(['r','p','s'])
    print(f"computer's choice is {computer}")
    if user == computer:
        return "tie"
    if is_win(user,computer) :
        return "you won"
    return "you lost"

def is_win(player,opponent) :
    #r>s ,s >p ,p>r
    if (player=='r' and opponent == 's')or(player =='s' and opponent =='p')or (player=='p' and opponent=="r"):
        return True
    
print(play())

    
    

         
