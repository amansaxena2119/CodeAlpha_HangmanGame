import random

# Predefined list of 5 words
words = ["apple", "bread", "chair", "dance", "eagle"]

# Randomly choose a word
word_to_guess = random.choice(words)
guessed_letters = []
tries_left = 6

# Create a display version of the word with underscores
display_word = ["_"] * len(word_to_guess)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while tries_left > 0 and "_" in display_word:
    print("Word: " + " ".join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Tries left: {tries_left}")
    
    guess = input("Enter a letter: ").lower()
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.\n")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        # Update the display word
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[index] = guess
        print("Good guess!\n")
    else:
        tries_left -= 1
        print("Wrong guess.\n")

# End of game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game over. The word was:", word_to_guess)
