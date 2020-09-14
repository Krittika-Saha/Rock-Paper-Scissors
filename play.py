wish = input()

def lets_cheat(option):
    if option == 'paper':
        print("Sorry, but the computer chose scissors")
    elif option == 'rock':
        print("Sorry, but the computer chose paper")
    elif option == 'scissors':
        print("Sorry, but the computer chose rock")
    
lets_cheat(wish)