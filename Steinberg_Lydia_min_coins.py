# I copied over takeInt from Steinberg_Lydia_loops.py and changed it for this program. I would normally just reference it, but this will be easier for you to check.
def takeInt(inputPrompt, keyWord = None, limit = None): # optionally takes a keyWord to check for
    inputStr = input(inputPrompt)
    inputInt = None # inputInt remains None until a valid input is given
    if (keyWord is not None) and (str(inputStr).lower() == str(keyWord)): # Check for inputInt.lower() to make the check case-insensitive.
            return keyWord # if the word is a particular one the task is looking for other than a number, returns that instead. If using this, should check for it before using inputInt as an int.
    else:
        try:
            inputInt = int(inputStr) # tries converting input to an int
            if (type(limit) == tuple): # I could also use a range here, in which case I'd need to use limit[-1] instead of limit[1] for the upper limit value.
                if inputInt in limit:
                    pass
                elif inputInt > limit[1]: # check upper limit
                    print(f"This input is above the range {limit[0]}-{limit[1]}. Please try again.")
                    inputInt = None
                    while inputInt is None:
                        inputInt = takeInt(inputPrompt, keyWord) # runs again until a valid input is given
                elif inputInt < limit[0]: # check lower limit
                    print(f"This input is below the range {limit[0]}-{limit[1]}. Please try again.")
                    inputInt = None
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
    keyWord = "0"
    change = None
    while change != keyWord:
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
        change = takeInt("Please Enter Amount of Change (1-99) or ZERO to EXIT.\n\n>", keyWord, (1,99))
        if change == keyWord:
            break
        else:
            while change >= 25: # quarters
                change -= 25
                quarters += 1
            while change >= 10: # dimes
                change -= 10
                dimes += 1
            while change >= 5: # nickels
                change -= 5
                nickels += 1

            pennies = change # pennies will be the remaining value in {change}

            print(f"\nQuarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}\n")

def main():
    min_coins()

main()