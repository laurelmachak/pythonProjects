import random

guessesTaken = 0

print("Welcome! What is your name?")
userName = input()

number = random.randint(1, 20)
print("Alright, " + userName  + ", I am thinking of a number between 1 & 20.")

for i in range(6):
    print("Take a guess")
    guess = int(input())
    
    if guess < number:
        print("your guess is too low")
        
    if guess > number:
        print("your guess is too high")
        
    if guess == number:
        break
