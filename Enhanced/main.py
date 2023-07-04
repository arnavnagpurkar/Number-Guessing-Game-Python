import random

def game():
    lowerBound = int(input("Enter the lower bound: "))
    upperBound = int(input("Enter the upper bound: "))

    number = random.randint(lowerBound, upperBound)

    if(lowerBound == upperBound):
        print("Lower bound and Upper Bound can't be same.")
        print("Try again.")

    else:
        while True:
            userinp = int(input("Guess the Number: "))
            if(userinp == number):
                print("Correct Number Guessed!")
                break
            elif(userinp > number):
                print("Smaller number please: ")
            elif(userinp < number):
                print("Bigger number please: ")
            else:
                print("Something went wrong!")
                break

game()
while True:
    again = int(input("Want to play again?(Press 1 to play again and 2 to exit): "))
    if(again == 1):
        game()
    elif(again == 2):
        print("Thanks for playing!")
        break
    else:
        print("Invalid Input!")