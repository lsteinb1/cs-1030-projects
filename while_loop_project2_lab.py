# I wanted to do a try-except block in case either of the number inputs aren't entered as an integer, and making a function for it seemed like the best and easiest way to do so.

def takeInt(inputPrompt):
    inputInt = 0 # variable to return
    try:
        inputInt = int(input(inputPrompt))
    except:
        print("This input can't be converted to an integer. Please try again.")
        takeInt(inputPrompt) # runs again until a valid input is given
    return inputInt

def main():

    runAgain = True
    while runAgain == True:
        favNum = takeInt("What's your favorite number?: ")
        age = takeInt("How old are you?: ")
        name = input("What's your name?: ")

        print(f"{name}, your favorite number is {favNum} and you're {age} years old.")
        runAgain = False

        runAgain = input("Would you like to run the program again?: ")

        # runAgain.lower() to make each case-insensitive. Can take any case variation of 'y' or 'yes' for affirmative inputs, otherwise assumes no.
        if ((runAgain.lower() == "y") or (runAgain.lower() == "yes")):
            runAgain = True
        else:
            pass

main()