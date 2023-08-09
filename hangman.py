import random
from words import words

def get_valid_word(words):
    word = random.choice(words)                  #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangaman(): 
    word = get_valid_word(words)
    word_letters = set(word)            #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                #what the user has guessed 

user_input = input('Type something: ')
print(user_input)