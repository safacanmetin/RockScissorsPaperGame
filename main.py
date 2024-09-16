import random

def play():
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissors , what is your choice? \n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return "Tie"
    
    # r > s , s > p , p > r
    if is_win(user,computer):
        return "You won! Computer was {0}".format(computer)
    return "You lost! Computer was {0}...".format(computer)
    
def is_win(player,opponent):
    if (player == 'p' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())    