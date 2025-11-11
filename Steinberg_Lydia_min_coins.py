# I copied over takeInt from Steinberg_Lydia_loops.py and changed it for this program. I would normally just reference it, but this will be easier for you to check.
def takeInt(inputPrompt, keyWord = None, limit = None): # optionally takes a keyWord to check for
    inputStr = input(inputPrompt)
    inputInt = None # inputInt remains None until a valid input is given
    if (keyWord is not None) and (str(inputStr).lower() == str(keyWord)): # Check for inputInt.lower() to make the check case-insensitive.
            return keyWord # if the word is a particular one the task is looking for other than a number, returns that instead. If using this, should check for it before using inputInt as an int.
    else:
        try:
            inputInt = int(inputStr) # tries converting input to an int
            if (type(limit) == range):
                if inputInt in limit:
                    pass
                elif inputInt > limit[1]:
                    print(f"This input is above the range {limit[0]}-{limit[1]}. Please try again.")
                    while inputInt is None:
                        inputInt = takeInt(inputPrompt, keyWord) # runs again until a valid input is given
                elif inputInt < limit[0]:
                    print(f"This input is below the range {limit[0]}-{limit[1]}. Please try again.")
                    while inputInt is None:
                        inputInt = takeInt(inputPrompt, keyWord) # runs again until a valid input is given
        except ValueError:
            if (keyWord is not None):
                print(f"This input can't be converted to an integer and isn't keyword '{keyWord}'. Please try again.")
                while inputInt is None:
                    inputInt = takeInt(inputPrompt, keyWord) # runs again until a valid input is given
            else:
                print("This input can't be converted to an integer. Please try again.")
                while inputInt is None:
                    inputInt = takeInt(inputPrompt) # runs again until a valid input is given
    return inputInt

def min_coins():
    change = takeInt("Please Enter Amount of Change (1-99) or ZERO to EXIT. ", 0, range(1,100))
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    
    print(change)

def main():
    min_coins()

main()