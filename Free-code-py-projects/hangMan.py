import random
from wordshangman import words
import string

def getWords(words):
    word = random.choice(words)
    return word.upper()

def getRemainingWord(word,userletters):
    for s in word:
        if(s in userletters):
            print(s, end=" ")
        else:
            print("_", end=" ")
    print()                   
  
    

def hangman():
    word = getWords(words)
    word_letters = set(word) #converts the string word into a set of unique characters.
    alphabet = set(string.ascii_uppercase)
    user_letters = set()
    
    lives = 7
    
    while(len(word_letters)>0 and lives>0):
        user_input = input("Guess a word: ").upper()
        
        if(user_input in user_letters):
            print("ahhhhh.. you already used that word, try again")
            continue
        
        user_letters.add(user_input)
        if(user_input in word_letters):
            print("You got the right word: ",user_input)
            word_letters.remove(user_input)
            getRemainingWord(word,user_letters)
        else:
            lives-=1
            print(f"you got it wrong, you got {lives} remaining")
            getRemainingWord(word,user_letters)
    
    
    
    if(lives==0):
        print("you died!! try again, this is the word: ",word)
    else:
        print("yayy!! you won, this is the word: ",word)       
       
hangman()       