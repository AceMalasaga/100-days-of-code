import random
import banner
LEVEL_EASY = 10
LEVEL_HARD = 5

def level_difficulty():
    level_diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level_diff == "easy":
        return LEVEL_EASY
    else:
        return LEVEL_HARD

def check_guess(user_guess, random_number):
    if user_guess == random_number:
        return f"You got it! The answer was {random_number}."
    elif user_guess > random_number:
        return "Too high!"
    else:
        return "Too low!"

def play_game():
    print(banner.logo)
    print("Welcome to the Guess Game!")
    print("I am thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    difficulty = level_difficulty()
    while difficulty > 0:
        print(f"You have {difficulty} attempts remaining to guess the number.")
        make_guess = int(input("Make a guess: "))
        correct_answer = check_guess(make_guess, random_number)
        print(check_guess(make_guess, random_number))
        if correct_answer == f"You got it! The answer was {random_number}.":
            return
        difficulty -= 1
    print("You've run out of guesses. Refresh the page to run again.")
play_game()

