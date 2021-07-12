import random


def loop():
    play_again = ' '
    play_again = input("Want to play again? (Y/N): ").lower()
    while play_again == 'y':
        play()
    print("Thank you for playing!Hope you had fun!!")


def play():
    print("'r' for Rock 'p' for Paper 's' for Scissor")
    user = input("Your Choice: ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computers Choice:{computer} \n")

    if user == computer:
        print('It\'s a tie!')
        loop()

    elif is_win(user, computer):
        print("You won!")
        loop()

    else:
        print("Computer won!")
        loop()


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == "r"):
        return True


play()
