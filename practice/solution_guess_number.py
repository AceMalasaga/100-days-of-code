import random
import banner

EASY_TURNS = 10
HARD_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS


def play_game():
    print(banner.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Direct selection & calculation
    answer = random.randint(1, 100)
    turns = set_difficulty()

    make_guess = 0
    while make_guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        make_guess = int(input("Make a guess: "))

        if make_guess > answer:
            print("Too high!\nGuess again!")
            turns -= 1
        elif make_guess < answer:
            print("Too low!\nGuess again!")
            turns -= 1
        else:
            print(f"You got it! The answer was {answer}.")
            return

    if turns == 0:
        print(f"You've run out of guesses, you lose! The answer was {answer}.")


play_game()