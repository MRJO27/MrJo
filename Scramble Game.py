import random

words = ["python", "apple", "java", "class", "program"]
def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def play_scramble_game():
    original_word = random.choice(words)
    scrambled_word = scramble_word(original_word)
    
    print("Welcome to the Word Scramble Game!")
    print("Try to guess the original word.")
    
    print(f"Scrambled word: {scrambled_word}")
    
    attempts = 5
    
    while attempts > 0:
        guess = input("Your guess: ").strip()
        
        if not guess:
            print("Invalid input please enter a word")
            continue
        
        if guess == original_word:
            print("Congratulation! You guessed Word Correctly")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts left.")
            else:
                print(f"Sorry, you have run out of attempts. The correct word was '{original_word}'.")
        
        break

play_scramble_game()






