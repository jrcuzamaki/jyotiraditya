import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

# Function to handle the player's guess
def guess_number():
    while True:
        try:
            guess = int(input("Take a guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main game loop
while True:
    player_guess = guess_number()

    if player_guess < secret_number:
        print("Too low. Try again!")
    elif player_guess > secret_number:
        print("Too high. Try again!")
    else:
        print("Congratulations! You guessed the number correctly!")
        break

print(f"The secret number was {secret_number}. Thanks for playing!")
