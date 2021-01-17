import random
def guessthenum():
    m=random.randint(1,8)
    while (True) :


         n=int(input("Guess a number between 1 and 8: "))


         if m==n :
             print("Correct Guess")
             break
         else:
             print("Incorrect guess",f"You are off the correct answer by {m-n}" , "Try again")
guessthenum()
