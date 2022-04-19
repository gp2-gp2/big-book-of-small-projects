import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        """Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
    
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
  Pico          One digit is correct but in the wrong position.
  Fermi         One digit is correct and in the right position.
  Bagels        No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""".format(
            NUM_DIGITS
        )
    )

    while True:
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        num_guesses = 1


def get_secret_num():
    pass


if __name__ == "__main__":
    main()
