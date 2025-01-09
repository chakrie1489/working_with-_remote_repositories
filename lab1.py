import random

def start_game():
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
    while True:
        choice = input("Do you want to play again? yes/no: ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. type 'yes' or 'no'.")

while True:
    start_game()
    if not play_again():
        print("Bye")
        break