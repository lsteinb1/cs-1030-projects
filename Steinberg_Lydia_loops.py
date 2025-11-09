import random # for optional use in guess_number

# I copied over takeInt from when I wrote it in project2_lab, then made several changes.
def takeInt(inputPrompt, keyWord = None): # optionally takes a keyWord to check for
    inputStr = input(inputPrompt)
    inputInt = None # inputInt remains None until a valid input is given
    try:
        inputInt = int(inputStr) # tries converting input to an int
    except:
        if (keyWord is not None) and (str(inputStr).lower() == keyWord): # Check for inputInt.lower() to make the check case-insensitive.
            return keyWord # if the word is a particular one the task is looking for other than a number, returns that instead. If using this, should check for it before using inputInt as an int.
        elif (keyWord is not None):
            print(f"This input can't be converted to an integer and isn't keyword '{keyWord}'. Please try again.")
            while inputInt is None:
                inputInt = takeInt(inputPrompt, keyWord) # runs again until a valid input is given
        else:
            print("This input can't be converted to an integer. Please try again.")
            while inputInt is None:
                inputInt = takeInt(inputPrompt) # runs again until a valid input is given
    return inputInt

def check_extremes(n, prev_n, lowest, highest): # for use in min_max and data_stats
    if (lowest is not None) and (highest is not None):
        if n >= prev_n: # checking how high the number is
            if n >= highest: # if >= the current highest number
                highest = n
        elif n <= prev_n: # checking how low the number is
            if (n <= lowest):
                lowest = n
    else:
        if lowest is None: # if lowest was previously undefined, this number becomes the new lowest
            lowest = n
        if highest is None: # if highest was previously undefined, this number becomes the new highest. this isn't an elif because at least the first number inputted will be both the lowest and the highest, so both of these should run
            highest = n
    return lowest, highest

def count(): # Task 1
    print("--- Counting numbers from 1 to 12. ---") # explaining each task about to be done, for the purpose of this assignment
    num = 0
    i = 0
    for i in range(1, 13): # stops at 13, doesn't print it
        num = i
        print(num)
        i += 1

def accumulate(): # Task 2
    print("--- Printing the sum of every integer from 1 and 200. ---")
    task2Sum = 0
    i = 1
    while i <= 200:
        task2Sum += i
        # print(i, task2Sum) # can remove the comment here to watch its process
        i += 1 # iterating this at the end so i could start at 1, for increased readability for i <= 200
    print(f"Sum 1...200 = {task2Sum}")

def evens(): # Task 3
    print("--- Printing every even number from 0 to 30. ---")
    i = 0
    even_num = 0
    for i in range(0, 31, 2):
        even_num = i
        if i != 30: # if it's the starting number or any of the numbers in between the start and end, end with space, no newline (also added a comma at each end for aesthetic purposes)
            print(even_num, end = ", ")
        else: # if it's the last one, we'll want to at least end with a newline, so the next task doesn't display on the same line
            print("and", even_num, end = ".\n")

def mult_table(): # Task 4
    print("--- Printing a multiplication table for a given integer. ---")
    k = takeInt("Input an integer: ") # input validation, converts to an int if possible
    i = 0
    for i in range(1, 11):
        print(f"{k} × {i} = ", k * i)

def n_numbers(): # Task 5
    print("--- Taking a user-determined amount of numbers, printing them, and printing their sum and average. ---")
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

def min_max(): # Task 6
    print("--- Taking input integers until user enters 'done', then printing the highest and lowest integers entered. ---")
    numbers = []
    n = 0
    keyWord = "done"
    highest = None
    lowest = None
    while n != keyWord:
        prev_n = n # previously inputted value; will be 0 in the first run
        n = takeInt("Input integers or type 'done': ", keyWord)
        if n != keyWord:
            numbers.append(n)
            extremes = check_extremes(n, prev_n, lowest, highest)
            lowest = extremes[0]
            highest = extremes[1]
    print(f"Highest number: {highest}, Lowest number: {lowest}")

def count_vowels(): # Task 7
    print("--- Counting the vowels (including a, e, i, o, and u) in an inputted word. ---")
    word = input("Enter a word: ")
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
    print(f"The word '{word}' contains {vowel_count} vowels.")

def data_stats(): # Task 8
    print("--- Giving information (count, sum, min, and max) about a list. ---")
    data = [12, 3, 7, 7, 20, -2, 0, 15, 15, 9]
    count = {} # full count. Used to determine duplicates
    duplicates = {}
    non_dupes = {}
    sum = 0
    lowest = None
    highest = None
    n = 0
    dupes_msg = "" # for formatting the message counting the duplicates
    count_msg = "There is one instance each of "
    for i in range(len(data)):
        prev_n = n
        n = data[i]
        sum += n
        if n in count: # a duplicate number
            count[n] += 1
            non_dupes.pop(n)
            count_msg = count_msg.replace(f"{n}, ", "")
            duplicates[n] = count[n]
            dupes_msg += f"There are {count[n]} instances of {n}. "
        else:
            count[n] = 1
            non_dupes[n] = count[n]
            if i != len(data) - 1: # if not on last run
                count_msg += f"{n}, "
            else:
                count_msg += f"and {n}."
        extremes = check_extremes(n, prev_n, lowest, highest)
        lowest = extremes[0]
        highest = extremes[1]
    print(f"Count: There are {len(data)} items in the data. {count_msg} {dupes_msg}", f"Sum: {sum}, Min: {lowest}, Max: {highest}")

def guess_number(first_run = True): # Task 9
    num_range = [0, 30]
    if first_run: # I don't need to display this on repeated runs
        print(f"--- Letting the user try to guess a number between {num_range[0]} and {num_range[1]}. ---")
    secret_number = random.randint(num_range[0], num_range[1]) # can also just set this to 17 for testing purposes
    attempts = 5
    right_guess = False
    for i in range(attempts):
        guess = takeInt("Input the number you'd like to guess: ")
        if guess == secret_number:
            print(f"Correct! The secret number is {secret_number}.")
            right_guess = True
            break
        elif guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
    if right_guess == True:
        print("Nice!", end = " ")
    else:
        print(f"You've run out of attempts to guess. The secret number was {secret_number}.")
    play_again = input("Would you like to play again?: ")
    if (str(play_again).lower() == "yes") or (str(play_again).lower() == "y"):
        guess_number(False)

def ASCII_rectangle(): # Task 10
    print("--- Takes width and height and prints an ASCII rectangle with the given dimensions. ---")
    width = takeInt("Please enter rectangle width: ")
    height = takeInt("Please enter rectangle height: ")
    for i in range(height):
        if i != 0:
            print("", end="\n") # adds a newline for every new row (not including the first so it doesn't start with one)
        for j in range(width):
            if (i == 0 or i == height - 1) or (j == 0 or j == width - 1): # if at the beginning or end of the loop (first row or last row; top and bottom edges of the rectangle) or the beginning or end of the row (left and right edges)
                print("#", end="")
            else:
                print(" ", end="") # empty space if not on an edge, so the rectangle is hollow

def main():
    count()
    accumulate()
    evens()
    mult_table()
    n_numbers()
    min_max()
    count_vowels()
    data_stats()
    guess_number()
    ASCII_rectangle()

main()