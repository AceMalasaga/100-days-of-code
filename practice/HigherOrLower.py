import random
import game_data
import banner

def rand_personality():
    """Randomly generate a personality from game_data.data"""
    person = random.choice(game_data.data)
    return person

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
    if follower1 > follower2:
        return 'A'
    else:
        return 'B'

def play_game():
    score = 0
    game_should_continue = True
    compare_a = rand_personality()
    print(banner.banner_high)
    while game_should_continue:
        compare_b = rand_personality()
        #If compare_a and compare_b are the same pick a new compare_b from personality function
        while compare_a == compare_b:
            compare_b = rand_personality()
        format_a = per_format(compare_a)
        print(f"Compare A: {format_a}")
        print(banner.banner_vs)
        format_b = per_format(compare_b)
        print(f"Against B: {format_b}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        correct_answer = check_winner(compare_a, compare_b)
        if guess == correct_answer:
            score += 1
            if correct_answer == 'B':
                compare_a = compare_b
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False
play_game()