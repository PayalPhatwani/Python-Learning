import random
def play():
    user = input("Choose a choice: R for Rock, P for Paper,S for Scissor: ").upper()
    print("YOU SELECT: ",user)
    computer = random.choice(['R','S','P'])
    
    if(user==computer):
        return"It's a Tieeeee"
    
    if (win(user,computer)):
        return "Yayyyy!! you win..."
    else:
        return "you lost, Try again !!!"
    

def win(user,computer):
    
    if (user =='R' and computer=='S') or (user =='S' and computer=='P') or (user =='P' and computer=='R'):
        return True
    else:
        return False


print(play())  
        
        