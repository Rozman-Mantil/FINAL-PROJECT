import random
import string

def generate_password(length=12):
    """Generate a random alphanumeric password."""
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
