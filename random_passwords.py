import random
import string

def generate_random_password(length=12):
    """
    Generate a random password with a mix of uppercase, lowercase, digits, and symbols.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate 1000 random passwords
num_passwords = 1000
passwords = [generate_random_password() for _ in range(num_passwords)]

# Save to a file
with open("random_passwords.txt", "w") as file:
    # file.write("Password\n")  # Add a header
    for password in passwords:
        file.write(password + "\n")

print(f"{num_passwords} random passwords have been generated and saved to 'random_passwords.txt'.")
