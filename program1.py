def evens():
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
    # evens()
    # mult_table()
    n_numbers()

main()