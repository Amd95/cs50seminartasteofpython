import random

def main():

    #Countdown to the New Year
    number = random.randint(5,15)
    countdown(number)
    print("Happy New Year!")

def countdown(n):
    for i in range(n):
        print(n - i)

main()
