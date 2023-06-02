import random

def play_game():
    words = ["python", "programming", "computer", "hangman", "code"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("=== Hangman ===")
    print("Tebak kata:", end=" ")
    display_word(secret_word, guessed_letters)

    while True:
        guess = get_letter_guess()

        if guess in guessed_letters:
            print("Anda sudah menebak huruf ini sebelumnya. Coba lagi!")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Tebakan Anda benar!")
            display_word(secret_word, guessed_letters)
        else:
            attempts -= 1
            print("Tebakan Anda salah.")
            print_hangman(attempts)

            if attempts == 0:
                print("Anda kalah! Kata yang benar adalah:", secret_word)
                break

        if all_letters_guessed(secret_word, guessed_letters):
            print("Selamat, Anda menang!")
            break

def display_word(secret_word, guessed_letters):
    for char in secret_word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

def get_letter_guess():
    while True:
        guess = input("Tebak huruf: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Masukkan hanya satu huruf.")
        else:
            return guess

def all_letters_guessed(secret_word, guessed_letters):
    for char in secret_word:
        if char not in guessed_letters:
            return False
    return True

def print_hangman(attempts):
    stages = [
        """
            -----
            |   |
            |   O
            |  /|\\
            |  / \\
            |
        """,
        """
            -----
            |   |
            |   O
            |  /|\\
            |  /
            |
        """,
        """
            -----
            |   |
            |   O
            |  /|\\
            |
            |
        """,
        """
            -----
            |   |
            |   O
            |  /|
            |
            |
        """,
        """
            -----
            |   |
            |   O
            |   |
            |
            |
        """,
        """
            -----
            |   |
            |   O
            |
            |
            |
        """,
        """
            -----
            |   |
            |
            |
            |
            |
        """
    ]
    print(stages[6 - attempts])

def main():
    play_game()

if __name__ == "__main__":
    main()
