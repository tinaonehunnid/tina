import random


secret_number = random.randint(1,10)


print("Guess a number between 1 and 10. You have three attempts.")


for attempt in range(3):
    guess = int(input("enter your guess "))
    if guess == secret_number:
        print ("congrats, you're a muthafuckin gangsta dawg")
        break
    elif guess < secret_number:
        print ("too low, I think Mcdicks is hiring")
    else: 
        print ("you suck")


if guess != secret_number:   
    print(f"the secret number was {secret_number}.")

