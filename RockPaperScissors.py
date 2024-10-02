import random
number = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors:\n"))

# Check for invalid input
if number < 0 or number > 2:
    print("You chose an invalid number. Please choose 0, 1, or 2.")
else:
    # Display player's choice
    if number == 0:
        print("You chose Rock:")
        print(rock)
    elif number == 1:
        print("You chose Paper:")
        print(paper)
    else:
        print("You chose Scissors:")
        print(scissors)

    # Computer's choice
    print("Computer Choice:")
    random_name = random.randint(0, 2)
    options = ["Rock", "Paper", "Scissors"]
    print(options[random_name])

    if random_name == 0:
        print(rock)
    elif random_name == 1:
        print(paper)
    else:
        print(scissors)

    # Determine the outcome
    if random_name == number:
        print("It's a draw!")
    elif (number == 0 and random_name == 2) or (number == 1 and random_name == 0) or (number == 2 and random_name == 1):
        print("You Win!")
    else:
        print("You Lose!")
