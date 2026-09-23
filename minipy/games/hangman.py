import random

hangman = [
    r"""
    -----
      ;   
      
     
      
     
    _____
    """,
    r"""
    -----
      ;   
      O
     
      
     
    _____
    """,
    r"""
    -----
      ;   
      O
      |
      |
     
    _____
    """,
    r"""
    -----
      ;   
      O
     /|
      |
     
    _____
    """,
    r"""
    -----
      ;   
      O
     /|\
      |
     
    _____
    """,
    r"""
    -----
      ;   
      O
     /|\
      |
     / 
    _____
    """,
    r"""
    -----
      ;   
      O
     /|\
      |
     / \
    _____
    """
]

hangman.reverse()

word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

def game():
    word = random.choice(word_list)
    guessword = ["_"] * len(word)
    
    attempts = len(hangman) - 1
    wrong = 0
    guesses = []
    
    while attempts > 0:
        print("\n" + hangman[wrong])
        
        colored = []
        for letter in guesses:
            if letter in word:
                colored.append("\033[1m\033[92m" + letter.upper() + "\033[0m")
            else:
                colored.append("\033[1m\033[91m" + letter.upper() + "\033[0m")
        
        print(f"Already guessed: " + ", ".join(colored))
        print("\nCurrent word: "+" ".join(guessword))

        guess = input("Enter a letter: ").strip().lower()
        guesses.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessword[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            wrong += 1
            print("Wrong guess! Attempts left: "+ str(attempts))
        
        if "_" not in guessword:
            print("\nCongratulations! You guessed the word: "+ word)
            break
    
    if attempts == 0 and "_" in guessword:
        print("\nYou've run out of attempts! The word was: "+ word)

while True:
    game()
    
    restart = input("\nDo you want to restart? (Y/N): ").strip().lower()
    if restart != "y":
        print("Thanks for playing!")
        break
                    
                