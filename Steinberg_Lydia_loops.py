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
    even_num = 0
    for i in range(0, 31, 2):
        even_num = i
        print(even_num, end = " ")

def mult_table():
    k = int(input("Input an integer: "))
    i = 0
    for i in range(1, 11):
        print(f"{k} × {i} = ", k * i)

def n_numbers():
    n = 1
    try:
        n = int(input("How many numbers would you like to enter?: "))
    except:
        pass
    i = 0
    numbers = []
    num_sum = 0
    num_avg = 0
    for i in range(n):
        num = int(input("Input an integer: "))
        numbers.append(num)
        num_sum += num
    i = 0
    print("Entered numbers:", end = " ")
    for i in range(n):
        if i != n:
            print(numbers[i], end = ", ")
        else:
            print(numbers[i], end = ".")
    num_avg = (num_sum / n)
    print(f"Sum: {num_sum}, Average: {num_avg}")


def main():
    count()
    add()
    evens()
    mult_table()
    n_numbers()

main()