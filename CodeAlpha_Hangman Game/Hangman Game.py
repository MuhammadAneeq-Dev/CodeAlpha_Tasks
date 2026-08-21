import random

words = ["python", "laptop", "coding", "program", "gaming"]

word = random.choice(words)
guessed_word = ["_"] * len(word)

wrong_guesses = 0
guessed_letters = []

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

while wrong_guesses < 6 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses left:", 6 - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)