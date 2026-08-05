import random
import banner
guess = 0

def is_random():
    rand_num = random.randint(1, 100)
    return rand_num

def number_guess(num_guess):
    diff = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if diff == "easy":
        return num_guess + 10
    else:
        return num_guess + 5

def check_guess():
    random_number = is_random()
    guess_num = number_guess(guess)
    while guess_num > 0:
        print(f"You have {guess_num} attempts remaining to guess the number.")
        guess_num -= 1
        make_guess = int(input("Make a guess: "))
        if make_guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            return
        elif make_guess > random_number:
            print("Too high!")
            print("Guess again!")
        else:
            print("Too low!")
            print("Guess again!")
    print("You've run out of guesses. Refresh the page to run again.")

def play_game():
    print(banner.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    check_guess()

play_game()