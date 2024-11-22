import random
import string

def password_generator():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters. Try again!")
            return password_generator()
    except ValueError:
        print("Please enter a valid number!")
        return password_generator()
    print("Choose the complexity level of your password:")
    print("1. Numbers only")
    print("2. Letters only")
    print("3. Letters and numbers")
    print("4. Letters, numbers, and special characters")
    
    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
    except ValueError:
        print("Invalid choice! Please try again.")
        return password_generator()
    numbers = string.digits
    letters = string.ascii_letters
    special_chars = string.punctuation
    if choice == 1:
        char_pool = numbers
    elif choice == 2:
        char_pool = letters
    elif choice == 3:
        char_pool = letters + numbers
    elif choice == 4:
        char_pool = letters + numbers + special_chars
    else:
        print("Invalid choice! Please try again.")
        return password_generator()
    password = ''.join(random.choices(char_pool, k=length))
    print(f"Your generated password is: {password}")
password_generator()
