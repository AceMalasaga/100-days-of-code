import random

def find_treasure():
    treasures = [0, 5, 10, 15, 20]
    treasure = random.choice(treasures)
    return treasure


def user_turn():
    temporary_gold = 0
    is_continue_explore = True

    while is_continue_explore:
        found_treasure = find_treasure()

        if found_treasure == 0:
            print("TRAP! You lose all temporary gold.")
            return 0
        else:
            temporary_gold += found_treasure
            print(
                f"You found {found_treasure} gold! "
                f"Total: {temporary_gold}"
            )

        choice = input("Do you want to explore again? (y/n) ").lower()

        if choice != "y":
            is_continue_explore = False

    return temporary_gold


def computer_turn():
    temporary_gold = 0

    while temporary_gold < 25:
        found_treasure = find_treasure()

        if found_treasure == 0:
            print("TRAP! Computer loses all temporary gold.")
            return 0
        else:
            temporary_gold += found_treasure
            # print(
            #     f"Computer found {found_treasure} gold! "
            #     f"Total: {temporary_gold}"
            # )

    return temporary_gold


def check_win(user_gold, computer_gold):
    if user_gold >= 100:
        return "You win!"
    elif computer_gold >= 100:
        return "Computer wins!"
    else:
        return ""


def play_game():
    user_gold = 0
    computer_gold = 0

    while user_gold < 100 and computer_gold < 100:
        user_gold += user_turn()
        if user_gold >= 100:
            break
        else:
            computer_gold += computer_turn()
        print(check_win(user_gold, computer_gold))


while input(
    "Do you want to play again? (y/n) "
).lower() == "y":
    play_game()
    print("\n" * 3)
print("Thank you for playing!")