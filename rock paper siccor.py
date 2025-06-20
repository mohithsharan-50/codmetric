import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
            (player == "scissors" and computer == "paper") or \
            (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    choices = {"rock", "paper", "scissors"}

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if player_choice == 'exit':
            print("Thanks for playing!")
            break
        elif player_choice not in choices:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

main()
