import random 
choices = ['rock', 'paper', 'scissors']
    #defining game choices 

userChoice = input("Rock, Paper, Scissors! (Enter your choice): ").lower()
    #user's choice of play 

computerChoice = random.choice(choices)

print(f"Computer's choice {computerChoice}.")

#winner is determined! 
if userChoice == computerChoice:
    print("We both win!")
elif userChoice == 'rock':
    if computerChoice == 'paper':
        print("Sorry! You lose!")
    else:
        print("Yay! You win!")
elif userChoice == 'scissors':
    if computerChoice == 'rock':
        print("Sorry! You lose!")
    else:
        print("Yay! You win!")
elif userChoice == 'paper':
    if computerChoice == 'scissors':
        print("Sorry! You lose!")
    else:
        print("Yay! You win!")

else: 
    print("Invalid input. Rock, paper Scissors was not entered, try again.")