def count():
    print("Counting numbers from 1 to 12.")
    for i in range(1, 13):
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
    even_nums = []
    for i in range(0, 31, 2):
        even_nums.append(i)
    print(even_nums)

def multiplication_table():
    pass

def main():
    count()
    add()
    evens()
    multiplication_table()

main()