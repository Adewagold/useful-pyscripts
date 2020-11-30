from sys import argv
from random import randint
print(len(argv))
if len(argv) == 3:
    start = argv[1]
    end = argv[2]
else:
    print("Enter start and end date to start the game")
    exit(0)

number = randint(int(start), int(end))
attempt = 0
while True:
    try:
        attempt +=1
        guess = int(input("Guess the number: "))
        if guess ==number:
            print(f"You guessed correctly in {str(attempt)} attempt")
            break
        else:
            print("Wrong! Please try again")
    except ValueError as ex:
        print("Invalid Input! Please enter a valid input")
        continue
