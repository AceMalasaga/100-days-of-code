import random

def generate_room():
    rooms = [ "monster", "treasure", "treasure", "treasure", "treasure" ]
    room = random.choice(rooms)
    return room

def generate_gold():
    gold_values = [10, 20, 30]
    gold = random.choice(gold_values)
    return gold

def user_turn():
    temporary_gold = 0
    is_continue = True
    while is_continue:
        random_gold = generate_gold()
        random_room = generate_room()
        print(f"You found a {random_room} chest!")
        print(f"You collected {random_gold} gold.")
        print(f"Temporary Gold: {temporary_gold}")
        if random_room == "monster":
            print("MONSTER ATTACK! You lost all temporary gold.")
            return 0
        else:
            temporary_gold += random_gold
            user_choice = input("Would you like to enter another room? (y/n): ").lower()
            if user_choice != "y":
                is_continue = False
    return temporary_gold

def computer_turn():
    temporary_gold = 0
    is_continue = True
    while is_continue:
        random_gold = generate_gold()
        random_room = generate_room()
        if temporary_gold <= 50:
            if random_room == "monster":
                return 0
            else:
                temporary_gold += random_gold
            is_continue = False
    return temporary_gold

def check_winner(user_total, computer_total):
    if user_total >= 100:
        return "You escaped the dungeon!"
    elif computer_total >= 100:
        return "The computer escaped first!"
    else:
        return ""

def play_game():
    user_total = 0
    computer_total = 0

    while user_total < 100 and computer_total < 100:
        user_total += user_turn()
        if user_total >= 100:
            break
        else:
            computer_total += computer_turn()
        print("=========================")
        print(f"Your Total Gold: {user_total}")
        print(f"Computer Total Gold: {computer_total}")
        print("=========================")
    print("======== FINAL SCORE ========")
    print(f"You: {user_total} Gold")
    print(f"Computer: {computer_total} Gold")
    print(check_winner(user_total, computer_total))
    print("=========================")

while input("Do you want to enter the Monster Dungeon? (y/n)").lower() == "y":
    play_game()
    print("\n" * 3)
print("Thank you for playing Monster Dungeon!")