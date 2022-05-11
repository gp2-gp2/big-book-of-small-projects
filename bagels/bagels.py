"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100.


def main():
    print(
        f"""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
    
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
  Pico          One digit is correct but in the wrong position.
  Fermi         One digit is correct and in the right position.
  Bagels        No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico."""
    )

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(f" You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input(">>> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They are correct so, break out of this loop.
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        print("Do you want to play again? (yes or no)")
        if not input(">>> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def get_secret_num():
    pass


def get_clues():
    pass


if __name__ == "__main__":
    main()
