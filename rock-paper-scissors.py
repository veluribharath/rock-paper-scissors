import random

def is_win(user,computer):
    # returns True if you've won
    # r > s and s > p and p > r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return False
    
    return True

def play():
    user_choice = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer_choice = random.choice(['r','p','s'])
    
    if user_choice == computer_choice:
        return "It's a Tie! Try again!"
    
    if is_win(user_choice,computer_choice):
        return "You Won!"

    return "You Lost!"

def main():
    print(play())

if __name__ == "__main__":
    main()
