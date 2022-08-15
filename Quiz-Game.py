print("Welcome to Quiz Game")
playing = input("Want to play? \n Press 1: if you want to play \n Press 2: if you want to quit \n")

#quit function defined
def quit():
    print("****Have a good Day****")

if playing == "1":
    print("Okay! Let's play :) \n")
    score = 0
    count = 0
elif playing == "2":
    quit()
else:
    print("Press valid number!") 

questions = ["What is the full form of CPU?",
             "What is the full form RAM?", "What is the full form ROM?"]

answers = ["Central Processing Unit","Random Access Memory","Read Only Memory"]

#print(f"Total Score: {score}/{count}")
for i in range(len(questions)):
    answer = input(questions[i]+" ")
    if answer == answers[i]:
        score+=1
        print("Correct!")
    else:
        print("Wrong!")
    count+=1

print(f"Game Over \nYour score is: {score}")



    
