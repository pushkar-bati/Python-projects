import random
secret_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")
guess = int(input("Enter your guess: "))
while guess != secret_number:
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    guess = int(input("Enter your guess: "))
print("Correct")