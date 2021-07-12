import random


def guess(x):
    random_number = random.randint(1, x)
    guessedno = 0
    while guessedno != random_number:
        guessedno = int(input(f"Enter a number between 1 and {x}: "))
        if guessedno > random_number:
            print("Guess again.Too high")
        elif guessedno < random_number:
            print("Guess again.Too low")

    print(f"Congratulations!! You have guessed the random_number ={random_number} ")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            # This will give problem if low==high
            random_number = random.randint(low, high)
            print(random_number)
        else:
            random_number = low
        print("Menu:")
        print("Too high(H)")
        print("Too low(L)")
        print("Correct(C)")
        feedback = input("Your choice: ").upper()
        if feedback == 'L':
            low = random_number+1
        elif feedback == 'H':
            high = random_number-1

    print(f"Congratulations!! You have guessed the random_number ={random_number} ")
