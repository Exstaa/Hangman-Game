import random

words = ['python', "apple", "tomato", "banana"]

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    secret_word = choose_word(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\n", display_word(secret_word, guessed_letters))
        print("Attempts:", attempts)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed")
        elif guess in secret_word:
            guessed_letters.append(guess)
            if display_word(secret_word, guessed_letters) == secret_word:
                print("Congratulations! You guessed the word:", secret_word)
                break
        else:
            print("Incorrect guess")
            attempts -= 1

    if attempts == 0:
        print("Out of attempts The word was:", secret_word)

hangman()
