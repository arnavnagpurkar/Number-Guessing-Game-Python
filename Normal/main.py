import random


def game():
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))

    compint = random.randint(lower + 1, upper - 1)
    userinp = int(input(f"Guess the number between {lower} and {upper}: "))
    print(f"Number you entered is {userinp}\nThe number was {compint}")

    def again():
        print("Guess again?")
        print("1. Yes\n2. No")
        i = int(input("Enter choice(1/2): "))
        if i == 1:
            print("\n")
            game()
        elif i == 2:
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid Input!")
            again()

    if userinp == compint:
        print("You win!")
        again()
    elif userinp != compint:
        print("You lose!")
        again()


try:
    game()
except Exception as e:
    print(f"An error occurred, Error: \"{e}\"\nTrying again!\n")
    game()
