import random

NUM_DIGITS = 3
MAX_GUESSES = 10


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

    while True:
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input(">>> ")


def get_secret_num():
    pass


if __name__ == "__main__":
    main()
