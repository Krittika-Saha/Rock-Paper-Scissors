import random 
user = input()
while(user != "!exit"):
    choice_list = ["rock", "paper", "scissors"] 
    computer_choice = random.choice(choice_list)
    lost = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    
    if user not in choice_list:
        print("Invalid input") 
    elif lost[user] == computer_choice:
        print(f"Sorry, but computer chose {computer_choice}")
    elif computer_choice == user:
        print(f"There is a draw ({user})")
    else:
        print(f"Well done. The computer chose {computer_choice} and failed")
    user = input()
print("Bye!")