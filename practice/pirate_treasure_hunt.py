import random

def generate_island():
    events = ["treasure", "treasure", "treasure", "storm", "pirates"]
    random_island = random.choice(events)
    return random_island

def generate_gold():
    treasure = [20, 30, 40]
    random_gold = random.choice(treasure)
    return random_gold

def user_turn():
    temporary_gold = 0
    continue_voyage = True
    while continue_voyage:
        print("================================")
        island_treasure = generate_island()
        if island_treasure == "treasure":
            gold = generate_gold()
            temporary_gold += gold
            print(f"+{gold} gold")
        elif island_treasure == "storm":
            temporary_gold //= 2 # AI recommend to use // instead of /
            print("Half of your temporary gold was lost!")
        else:
            print("Pirates attacked!")
            return 0
        print(f"Temporary Gold: {temporary_gold}")
        user_choice = input("Sail to another island? (y/n)").lower()
        if user_choice == "n":
            break
    return temporary_gold

def computer_turn():
    temporary_gold = 0
    continue_voyage = True
    while continue_voyage:
        island_treasure = generate_island()
        if island_treasure == "treasure":
            gold = generate_gold() #AI recommend this
            temporary_gold += gold
        elif island_treasure == "storm":
            temporary_gold //= 2 # AI recommend to use // instead of /
        else:
            return 0
        if temporary_gold >= 80:
            break
    return temporary_gold

def check_winner(user_total, computer_total):
    if user_total >= 150:
        return "🏴‍☠️ You became the Pirate King!"
    elif computer_total >= 150:
        return "🏴‍☠️ Computer became the Pirate King!"
    elif user_total > computer_total: #AI recommend this
        return "🏴‍☠️ You became the Pirate King!"
    else: #AI recommend this
        return "🏴‍☠️ Computer became the Pirate King!"

def play_game():
    user_total = 0
    computer_total = 0
    while user_total < 150 and computer_total < 150: #AI recommend to use and not or
        user_total += user_turn()
        computer_total += computer_turn()
        if user_total >= 150 or computer_total >= 150:
            break
        # else:
        #     computer_total += computer_turn()
    print("=========================")
    print("FINAL RESULTS")
    print(f"Your total gold: {user_total}")
    print(f"Computer total gold: {computer_total}")
    print(check_winner(user_total, computer_total))
    print("=========================")

while input("Would you like to play again? (y/n)").lower() != "n":
    play_game()
    print("\n" * 2)