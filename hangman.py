import random

# List of words for the game
words = ['python', 'hangman', 'programming', 'developer', 'computer', 'algorithm', 'challenge']

def choose_word():
    """Select a random word from the word list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the current state of the word being guessed."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    """Main function to play Hangman."""
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Number of incorrect guesses allowed
    guessed_word = "_" * len(word)
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord to guess: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        
        # Ensure input is a single alphabetic letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
        
        # Check if the word is completely guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The correct word was: {word}")

if __name__ == "__main__":
    play_hangman()
