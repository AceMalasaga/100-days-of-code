import random

def find_crystal():
    value_crystal = [0, 10, 20, 30]
    crystal = random.choice(value_crystal)
    return crystal

def user_turn():
    temporary_crystal = 0
    exploring = True
    while exploring:
        value = find_crystal()
        if value == 0:
            print("ASTEROID HIT! You lost all temporary crystals.")
            return 0
        else:
            temporary_crystal += value
            print(f"You found {value} crystals.")
            print(f"You have {temporary_crystal} crystals.")
            user_choice = input("Explore another planet? (y/n)")
            if user_choice == "n":
                exploring = False
    return temporary_crystal
def computer_turn():
    temporary_crystal = 0
    exploring = True
    while exploring:
        value = find_crystal()
        if value == 0:
            print("ASTEROID HIT! Computer lost all temporary crystals.")
            return 0
        else:
            temporary_crystal += value
            if temporary_crystal >= 40:
                exploring = False
    return temporary_crystal

def check_winner(user_total, computer_total):
    if user_total >= 100:
        return "You win!"
    elif computer_total >= 100:
        return "Computer wins!"
    else:
        return ""

def play_game():
    user_total = 0
    computer_total = 0

    while user_total < 100 and computer_total < 100:
        user_total += user_turn()

        print("=========================")
        print(f"Your Total: {user_total}")
        print(f"Computer Total: {computer_total}")
        print("=========================")

        if user_total >= 100:
            break
        else:
            computer_total += computer_turn()
    print(check_winner(user_total, computer_total))
while input("Do you want to play again? (y/n)").lower() == "y":
    play_game()
    print("\n" * 5)
print("Thank you for playing!")