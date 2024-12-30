import random
import string

def generate_random_username():
    """
    Generate a random username.
    Format: [Adjective][Noun][RandomNumber]
    """
    adjectives = ["Swift", "Happy", "Brave", "Cool", "Funny", "Bright", "Clever", "Silent", "Gentle", "Fierce", "Mighty", "Rapid", "Kind", "Calm", "Shiny", "Witty", "Bold", "Charming"]
    nouns = ["Tiger", "Eagle", "Panda", "Dolphin", "Fox", "Wolf", "Hawk", "Lion", "Shark", "Falcon", "Bear", "Cheetah", "Otter", "Rabbit", "Panther", "Leopard", "Penguin", "Seal"]
    random_number = random.randint(100, 999)  # Generate a random number for uniqueness
    return f"{random.choice(adjectives)}{random.choice(nouns)}{random_number}".lower()

# Generate 1000 random usernames
num_usernames = 1000
usernames = [generate_random_username() for _ in range(num_usernames)]

# Save to a file
with open("random_usernames.txt", "w") as file:
    # file.write("Username\n")  # Add a header
    for username in usernames:
        file.write(username + "\n")

print(f"{num_usernames} random usernames have been generated and saved to 'random_usernames.txt'.")
