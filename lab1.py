"""
number guessing game
allows the users to play a simple guessing game".
"""

import random

def start_game():
    """
    starts the game.
    """
    print("Welcome to the number guessing game!")
    print("I have a number between 1 and 100 in my mind.")
    print(" try guessing it")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

def play_again():
    """
    function to play the game again if the player wishes so
    """
    while True:
        choice = input("Do you want to play again? yes/no: ").strip().lower()
        if choice == "yes":
            return True
        if choice == "no":
            return False
        print("Invalid input. type 'yes' or 'no'.")

def main():
    """
    main function.
    """
    while True:
        start_game()
        if not play_again():
            print("Goodbye! Thanks for playing.")
            break

if __name__ == "__main__":
    main()

while True:
    start_game()
    if not play_again():
        print("Bye")
        break
