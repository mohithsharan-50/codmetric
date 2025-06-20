import random

def number_guessing_game():

    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly.")
            print(f"It took you {attempts} attempts.")
            break


number_guessing_game()
