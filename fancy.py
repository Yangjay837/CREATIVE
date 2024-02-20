import random

def play_game():
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    play_game()