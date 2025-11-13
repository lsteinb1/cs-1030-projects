# I copied over takeInt from Steinberg_Lydia_loops.py and changed it for this program (including renaming it to takeNum to reflect being able to handle decimals). I would normally just reference it, but this will be easier for you to check.
def takeNum(inputPrompt, keyWord = None, limit = None, returnType = "int"): # optionally takes a keyWord to check for
    inputStr = input(inputPrompt)
    inputInt = None # inputInt remains None until a valid input is given
    if (keyWord is not None) and (str(inputStr).lower() == str(keyWord)): # Check for inputInt.lower() to make the check case-insensitive.
            return keyWord # if the word is a particular one the task is looking for other than a number, returns that instead. If using this, should check for it before using inputInt as an int.
    else:
        try:
            if returnType == "int":
                inputInt = int(inputStr) # tries converting input to an int
            elif returnType == "float":
                inputInt = float(inputStr)
            if (type(limit) == tuple): # I could also use a range here, in which case I'd need to use limit[-1] instead of limit[1] for the upper limit value.
                if (((limit[0] is not None and inputInt >= limit[0]) and (limit[1] is not None and inputInt <= limit[1])) or ((limit[1] is None) and (limit[0] is not None and inputInt >= limit[0])) or ((limit[0] is None) and (limit[1] is not None and inputInt <= limit[1]))): # if there is both a lower and upper limit and the input integer is between them, or if there is a lower limit but no upper limit and it's above that lower limit, or if there is an upper limit but no lower limit and it's below that upper limit
                    pass
                elif (limit[1] is not None) and (inputInt > limit[1]): # check upper limit, if there is one
                    print(f"This input is above the range {limit[0]}-{limit[1]}. Please try again.")
                    inputInt = None # reset so the int out of range isn't used
                    while inputInt is None:
                        inputInt = takeNum(inputPrompt, keyWord) # runs again until a valid input is given
                elif (limit[0] is not None) and (inputInt < limit[0]): # check lower limit, if there is one
                    print(f"This input is below the range {limit[0]}-{limit[1]}. Please try again.")
                    inputInt = None
                    while inputInt is None:
                        inputInt = takeNum(inputPrompt, keyWord) # runs again until a valid input is given
        except ValueError:
            if (keyWord is not None):
                print(f"This input can't be converted to an integer and isn't keyword '{keyWord}'. Please try again.")
                while inputInt is None:
                    inputInt = takeNum(inputPrompt, keyWord) # runs again until a valid input is given
            else:
                print("This input can't be converted to an integer. Please try again.")
                while inputInt is None:
                    inputInt = takeNum(inputPrompt) # runs again until a valid input is given
    return inputInt

def min_coins():
    keyWord = "0"
    change = None
    limit = (1,99) # (minimum, maximum). I could've also written this program around this value being a range.
    dollar_mode = True
    if dollar_mode:
        limit = (0,None)
    while change != keyWord:
        hundreds = 0
        fifties = 0
        twenties = 0
        tens = 0
        fives = 0
        ones = 0
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0

        quarter_amount = 0.25
        dime_amount = 0.10
        nickel_amount = 0.05
        penny_amount = 0.01

        if dollar_mode == False:
            change = takeNum("Please Enter Amount of Change (1-99) or ZERO to EXIT.\n\n>", keyWord, limit)
        else:
            change = takeNum("Please Enter Amount of Dollars and Change (1-99) or ZERO to EXIT.\n\n>", keyWord, limit, "float")
            print(change)
        if change == keyWord:
            break
        else:
            while change >= quarter_amount: # quarters
                change -= quarter_amount # subtract the amount of a quarter from change
                quarters += 1 # increase the count of quarters
                print(change)
            while change >= dime_amount: # dimes
                change -= dime_amount
                dimes += 1
                print(change)
            while change >= nickel_amount: # nickels
                change -= nickel_amount
                nickels += 1
                print(change)

            pennies = change # pennies will be the remaining value in {change}

            print(f"\nQuarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}\n")

def main():
    min_coins()

main()