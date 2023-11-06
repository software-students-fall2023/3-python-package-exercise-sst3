import random
import string
from words import words


def valid_word(words):
    word = random.choice(words["data"])
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = valid_word(words)
    print("worddd in hangman", word)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    tries = 6

    # getting user input
    while len(word_letters) > 0 and tries > 0:
        print(
            "You have",
            tries,
            "lives left.\nYou have used the letters:",
            " ".join(used_letters),
        )

        # word process
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        print("\n")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # correct guess
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                tries = tries - 1
                print(user_letter, "is not in word")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character")

    if tries == 0:
        print("\nNo more tries left. The word was", word)
    else:
        print("You guessed the word ", word, "correctly.")
