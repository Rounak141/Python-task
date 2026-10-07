import random

words = ["red", "blue", "green", "yellow","black", "white"]

secret_word = random.choice(words)

print("Welcome to Hangman Game!")
print("Choose a letter that is part of the name of a color.")

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

while incorrect_guesses < max_incorrect_guesses:

    display_word = ""

   
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break

else:
    print("\nGame Over!")
    print("The word was:", secret_word)