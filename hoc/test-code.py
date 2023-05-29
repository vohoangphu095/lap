import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a password with a length of 8 characters
password = generate_password(8)
print("Auto-generated password:", password)
