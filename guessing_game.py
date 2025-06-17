import random

def guessing_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Step 1: Generate a random number
    secret_number = random.randint(1, 100)

    # Step 2: Initialize attempt counter
    attempts = 0

    while True:
        try:
            # Step 3: Input from user
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Step 4: Check guess using if-elif-else
            if guess < secret_number:
                print("Too low! 📉 Try again.")
            elif guess > secret_number:
                print("Too high! 📈 Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

# Run the game
guessing_game()
