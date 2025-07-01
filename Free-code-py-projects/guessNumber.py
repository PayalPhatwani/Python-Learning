import random

def guess(x):
    random_num = random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess = int(input("Guess a number: "))
        
        if guess > random_num:
            print("You're guessing a bit high")
        elif guess<random_num:
            print("You're guessing a bit low")
    
    
    print(f"wohhoo you guessed it right its {random_num}=={guess}")        

# guess(5)


def computer_guess(x):
    low = 0
    high = x
    feedback=''
    
    while feedback!='c':
        c_guess = random.randint(low,high)
        feedback = input(f"is {c_guess} is the number: ")
        if feedback=='l':
            low=c_guess
        elif feedback=='h':
            high=c_guess    
    
    print(f"computer guessed it {c_guess}")    
    

computer_guess(10)    

    
    
    
    
                     