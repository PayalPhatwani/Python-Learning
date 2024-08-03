def replace_word():
    
    word = input("Enter a sentence")
    print("Here's the sentence:"+word)
    Check = input("Do you want to change word yes or no ?")
    
    if(Check.upper()=='yes' or Check.upper() == 'Y'):
        word_to_replace = input("Enter the word to replace:")
        if(0<word.find(word_to_replace)):
         word_replacement = input("Enter the word replacement:")
         print("Here's the result:-")
         print(word.replace(word_to_replace,word_replacement))
        else:
            print("The word you want to replace is not in the sentence, Try again !!")
    
    else:
        print("Okay! Have a great day")
        

replace_word()
    