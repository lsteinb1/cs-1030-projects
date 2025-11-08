# I copied over takeInt from when I wrote it in project2_lab, with several changes.
def takeInt(inputPrompt, keyWord = None):
    inputInt = input(inputPrompt) # prints 'inputPrompt' as the prompt for the input
    try:
        inputInt = int(inputInt) # tries converting to an int
        return inputInt
    except:
        if (keyWord != None) and (str(inputInt).lower() == keyWord): # Check for inputInt.lower() to make the check case-insensitive.
            return keyWord # if the word is a particular one the task is looking for other than a number, returns that instead. If using this, should check for it before using inputInt as an int. This is a bit of an inelegant solution for anything beyond the scope of this assignment, but it seemed most efficient for keeping the scope small.
        elif keyWord is not None:
            print(f"This input can't be converted to an integer and isn't isn't keyword '{keyWord}'. Please try again.")
            takeInt(inputPrompt, keyWord) # runs again until a valid input is given
        else:
            print("This input can't be converted to an integer. Please try again.")
            takeInt(inputPrompt) # runs again until a valid input is given

def intOrKeyword(inputPrompt, keyWord): # this function was necessary in addition to takeInt so I could run takeInt recursively in case of repeated invalid inputs, but still ensure the function I ran in the task returned a valid value at the end. There was probably a better way to do this, I'll revisit it if I have time.
    inputValue = None
    while inputValue is None:
        inputValue = takeInt(inputPrompt, keyWord)
    if str(inputValue).lower() == keyWord: # I'd like to make these checks less redundant if I have time later
        return keyWord
    else:
        return inputValue

def count(): # Task 1
    print("Counting numbers from 1 to 12.") # explaining the task about to be done, for the purpose of this assignment
    for i in range(1, 13): # stops at 13, doesn't print it
        print(i)
        i += 1

def accumulate(): # Task 2
    print("Printing the sum of every integer from 1 and 200.")
    task2Sum = 0
    i = 1
    while i <= 200:
        task2Sum += i
        # print(i, task2Sum) # can remove the comment here to watch its process
        i += 1 # iterating this at the end so i could start at 1, for increased readability for i <= 200
    print(f"Sum 1...200 = {task2Sum}")

def evens(): # Task 3
    print("Printing every even number from 0 to 30.")
    i = 0
    even_num = 0
    for i in range(0, 31, 2):
        even_num = i
        if i != 30: # if it's the starting number or any of the numbers in between the start and end, end with space, no newline (also added a comma at each end for aesthetic purposes)
            print(even_num, end = ", ")
        else: # if it's the last one, we'll want to at least end with a newline, so the next task doesn't display on the same line
            print("and", even_num, end = ".\n")

def mult_table(): # Task 4
    k = takeInt("Input an integer: ") # input validation, converts to an int if possible
    i = 0
    for i in range(1, 11):
        print(f"{k} × {i} = ", k * i)

def n_numbers(): # Task 5
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
    print("Taking input integers until user enters 'done', then printing the highest and lowest integers entered.")
    numbers = []
    n = 0
    keyWord = "done"
    highest = None
    lowest = None
    while n != keyWord:
        prev_n = n # previously inputted value; will be 0 in the first run
        n = intOrKeyword("Input integers or type 'done': ", keyWord)
        if n != keyWord:
            numbers.append(n)
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
    print(f"Highest number: {highest}, Lowest number: {lowest}")

def count_vowels(): # Task 7
    print("Counting the vowels (including a, e, i, o, and u) in an inputted word.")
    word = input("Enter a word: ")
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
    print(f"The word '{word}' contains {vowel_count} vowels.")

def data_stats(): # Task 8
    data = [12, 3, 7, 7, 20, -2, 0, 15, 15, 9]
    count = {}
    duplicates = {}
    non_dupes = {}
    sum = 0
    lowest = None
    highest = None
    n = 0
    dupes_msg = ""
    count_msg = "There is one instance each of "
    for i in range(len(data)):
        prev_n = n
        n = data[i]
        sum += n
        if n in count:
            count[n] += 1
            non_dupes.pop(n)
            duplicates[n] = count[n]
            dupes_msg += f"There are {count[n]} instances of {n}. "
        else:
            count[n] = 1
            non_dupes[n] = count[n]
            '''
            if i != len(data) - 1: # if not on last run
                count_msg += f"{n}, "
            else:
                count_msg += f"and {n}."
            '''
        if (lowest is not None) and (highest is not None): # these blocks copied from min_max. I would've preferred to make them a function to call in both related tasks, but I didn't realize that until later, so it'd be more complicated now. I'll do it if I have time.
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
    print(f"Count: {count_msg}{non_dupes.keys()} {dupes_msg}", "Sum: {sum}, Min: {lowest}, Max: {highest}")


def main():
    ''' count()
    accumulate()
    evens()
    mult_table()
    n_numbers()
    min_max()
    count_vowels()'''
    data_stats()

main()