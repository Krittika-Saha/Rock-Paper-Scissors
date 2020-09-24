import random 
name = input('Your Name:')
print(f"Hello, {name}!")
search = open("rating.txt", 'r+')
for line in search:
    line = line.rstrip()
    if name in line:
        slicing = line.split()
        rating = int(slicing[1])
    else:
        rating = 0
user = input("Your choice:")
while(user != "!exit"):
    choice_list = ["rock", "paper", "scissors"] 
    user_choice_list = ["rock", "paper", "scissors", '!rating'] 
    computer_choice = random.choice(choice_list)
    lost = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    if user == "!rating":
        print(rating)
    elif user not in user_choice_list:
        print("Invalid input") 
    elif lost[user] == computer_choice:
        print(f"Sorry, but computer chose {computer_choice}")
    elif computer_choice == user:
        print(f"There is a draw ({user})")
        rating += 50
    else:
        print(f"Well done. The computer chose {computer_choice} and failed")
        rating += 100
    user = input('Your Choice:')
search.write(f"\n{name} {rating}")
print("Bye!")