import random
import string
from pathlib import Path

def generate_password():
    """
    Generates a password composed of:
    - 3 simple words (2 random + 1 color)
    - A random two-digit number
    - A random simple special character
    Returns:
        str: The generated password
    """
    # Define a list of common colors
    common_colours = [
        "red", "blue", "green", "yellow", "orange",
        "purple", "pink", "brown", "black", "white", "gray"
    ]

    # Define simple special characters
    special_chars = ['!', '@', '#', '$', '%', '&', '*']

    # Choose a random color
    colour = random.choice(common_colours)

    # Define the path to the word list file
    word_file_path = Path.home() / "Code" / "simple_word_list.txt"

    # Load words from file
    try:
        with open(word_file_path, "r") as file:
            words = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return "Error: Word list file not found."

    # Select two random words
    selected_words = random.sample(words, 2)

    # Insert the color at a random position (0 or 1)
    selected_words.insert(random.randint(0, 1), colour)

    # Capitalize each word and join them
    base = ''.join(word.capitalize() for word in selected_words)

    # Add a random two-digit number
    number = str(random.randint(10, 99))

    # Add a random special character
    special = random.choice(special_chars)

    return base + number + special

def main():
    print("Press Enter to generate a new password. Close the window to exit.\n")
    try:
        while True:
            input()  # Wait for Enter key
            password = generate_password()
            print(f"Generated password: {password}")
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!") # Handle Ctrl+C gracefully

if __name__ == "__main__":
    main()