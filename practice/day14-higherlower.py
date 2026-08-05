import random
import game_data
import banner

print(banner.banner_high)


def personality():
    """Randomly generate a personality from game_data.data"""
    rand_personality = random.choice(game_data.data)
    return rand_personality

def per_format(formated_personality):
    """Format a personality according to the given format"""
    formated_personality = (f"{formated_personality['name']}, "
                            f"a {formated_personality['description']}, "
                            f"from {formated_personality['country']}")
    return formated_personality

def check_winner(per1, per2):
    """Compare two personality according to Follower Count and return a boolean"""
    follower1 = per1.get('follower_count')
    follower2 = per2.get('follower_count')
    print(f"this is personality {per1['name']}: {follower1}")
    print(f"this is personality {per2['name']}: {follower2}")
    if follower1 > follower2:
        return True
    else:
        return False

def play_game():
    score = 0
    game_should_continue = True
    compare_a = personality()
    while game_should_continue:
        print(f"Score {score}")
        compare_b = personality()
        #If compare_a and compare_b are the same pick a new compare_b from personality function
        while compare_a == compare_b:
            compare_b = personality()
        format_a = per_format(compare_a)
        print(f"Compare A: {format_a}")
        print(banner.banner_vs)
        format_b = per_format(compare_b)
        print(f"Against B: {format_b}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess == 'A':
            user_guess = compare_a
            if check_winner(user_guess, compare_b) == True:
                score += 1
            else:
                return
        else:
            user_guess = compare_b
            if check_winner(user_guess, compare_a) == True:
               score += 1
               compare_a = compare_b
            else:
                return

play_game()