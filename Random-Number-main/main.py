from codes import code

print("Menu:")
print("1.You guess the computer's secret number!")
print("2.The computer guesses your secret number!")
print("3.Exit")

choice = int(input("Your choice: "))

if choice == 1:
    code.guess(100)
elif choice == 2:
    code.computer_guess(100)
elif choice == 3:
    print("Goodbye!")
else:
    print("Wrong Choicee!")
