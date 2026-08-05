from game_data import data
import random
from banner import banner_high
from banner import banner_vs

print(banner_high)

def personality():
    """Select a random personality from the list called data then return it"""
    person = random.choice(data)
    return person

def format_data(person):
    """Return a formatted string representation of a personality dictionary."""
    formatted_person = f"{person['name']}, a {person['description']}, from {person['country']}"
    return formatted_person

def check_guess(person1, person2):
    """Check if two personalities are right"""
    if person1["follower_count"] > person2["follower_count"]:
        return "A"
    else:
        return "B"
def higher_or_lower():
    score = 0
    #Place this outside while so it will not erase everytime while loop iterate
    personality_a = personality()
    while True:
        personality_b = personality()
        formatted_a = format_data(personality_a)
        formatted_b = format_data(personality_b)
        #If compare_a and compare_b is the same select a new personality in the list
        while formatted_a == formatted_b:
            personality_b = personality()
            formatted_b = format_data(personality_b)
        print(f"Compare A: {formatted_a}")
        print(banner_vs)
        print(f"Against B: {formatted_b}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        correct_answer = check_guess(personality_a, personality_b)
        if guess == correct_answer:
            score += 1
            if correct_answer == "B":
                personality_a = personality_b
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            return
higher_or_lower()