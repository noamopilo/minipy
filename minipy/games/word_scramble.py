import random
from english_words import get_english_words_set
from wordfreq import zipf_frequency

all_words = list(get_english_words_set(["web2"], lower=True, alpha=True))

words = [word for word in all_words if zipf_frequency(word, "en") >=4]

def scramble_word():
    word = random.choice(words)
    scrambled_word = "" .join(random.sample(word, len(word)))
    return word, scrambled_word

word, scrambled_word = scramble_word()

attempts = 5
while attempts > 0:
    guess = input(f"Unscramble this word: {scrambled_word}: \n").lower()
    
    if guess == word:
        print(f"Correct!, The word was {word}")
        break
    else:
        attempts -= 1
        print(f"Wrong!, try again. Attempts left: {attempts}")

if attempts == 0:
    print(f"Game over!, The word was: {word}")

