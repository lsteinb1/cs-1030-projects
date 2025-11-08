# I copied over takeInt from when I wrote it in project2_lab, with several changes. I copied it instead of referencing the other file so it's easier for you to check it in this assignment
def takeInt(inputPrompt, checkWord = None):
    inputInt = input(inputPrompt) # prints 'inputPrompt' as the prompt for the input
    try:
        inputInt = int(inputInt) # tries converting to an int
        return inputInt
    except:
        if (checkWord != None) and (str(inputInt).lower() == checkWord): # Check for inputInt.lower() to make the check case-insensitive.
            print(inputInt, checkWord)
            return inputInt # if the word is a particular one the task is looking for other than a number, returns that instead. If using this, should check for it before using inputInt as an int. This is a bit of an inelegant solution for anything beyond the scope of this assignment, but it seemed most efficient for keeping the scope small.
        elif checkWord is not None:
            print("b")
            print("This input can't be converted to an integer. Please try again.")
            takeInt(inputPrompt, checkWord) # runs again until a valid input is given
        else:
            print("a")
            print("This input can't be converted to an integer. Please try again.")
            takeInt(inputPrompt) # runs again until a valid input is given

def intOrKeyword(inputPrompt, keyWord):
    inputValue = None;
    while inputValue is None:
    	inputValue = takeInt(inputPrompt, keyWord)
    if inputValue == keyWord:
        # Check for inputValue.lower() to make the check case-insensitive.
        print(inputValue, keyWord)
        return keyWord # if the word is a particular one the task is looking for other than a number, returns that instead. If using this, should check for it before using inputInt as an int. This is a bit of an inelegant solution for anything beyond the scope of this assignment, but it seemed most efficient for keeping the scope small.
    else:
        return inputValue

def count():
    print("Counting numbers from 1 to 12.") # explaining the task about to be done, for the purpose of this assignment
    for i in range(1, 13): # stops at 13, doesn't print it
        print(i)
        i += 1

def add():
    print("Printing the sum of every integer from 1 and 200.")
    task2Sum = 0
    i = 1
    while i <= 200:
        task2Sum += i
        print(i, task2Sum)
        i += 1 # iterating this at the end so i could start at 1, for increased readability for i <= 200

def evens():
    print("Printing every even number from 0 to 30.")
    i = 0
    even_num = 0
    for i in range(0, 31, 2):
        even_num = i
        if i != 30: # if it's the starting number or any of the numbers in between the start and end, end with space, no newline (also added a comma at each end for aesthetic purposes)
            print(even_num, end = ", ")
        else: # if it's the last one, we'll want to at least end with a newline, so the next task doesn't display on the same line
            print("and", even_num, end = ".\n")

def mult_table():
    k = takeInt("Input an integer: ") # input validation, converts to an int if possible
    i = 0
    for i in range(1, 11):
        print(f"{k} × {i} = ", k * i)

def n_numbers():
    n = 1
    n = takeInt("How many numbers would you like to enter?: ") # input validation
    i = 0 # initializing for future for loop
    input_numbers = [] # for storing the entered numbers
    num_sum = 0 # for storing the sum of the entered numbers
    num_avg = 0 # for storing the average of the entered numbers
    for i in range(n):
        num = takeInt("Input an integer: ") # input validation
        input_numbers.append(num)
        num_sum += num
    i = 0 # resetting count
    print("Entered numbers:", end = " ")
    for i in range(n):
        if i != n - 1: # if it isn't the last number
            print(input_numbers[i], end = ", ")
        else: # if it is the last number
            print(input_numbers[i], end = ". ")
    num_avg = (num_sum / n) # the sum divided by the number of integers entered
    print(f"Sum: {num_sum}, Average: {num_avg}")

def min_max():
    print("Taking input integers until user enters 'done', then printing the highest and lowest integers entered.")
    numbers = []
    n = 0
    keyWord = "done"
    while n != keyWord:
    	n = intOrKeyword("Input integers or type 'done': ", keyWord)
    	if n != keyWord:
    		numbers.append(n)
    print(numbers)


def main():
    ''' count()
    add()
    evens()
    mult_table()
    n_numbers()'''
    min_max()

main()