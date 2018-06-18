from math import sqrt


counter = 0
memo = {}


def reset_counter():
    global counter
    counter = 0


def add(a, b):
    global counter
    counter += 1
    return a + b


def fib_closed(n):
    return int(((1 + sqrt(5))**n - (1-sqrt(5))**n) / (2**n * sqrt(5)))


def fib_classic(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return add(fib_classic(n-2), fib_classic(n-1))


def fib_loop(n):
    a = 0
    b = 1
    if n == 0:
        b = 0
    else:
        for i in range(0, n-1):
            c = add(a, b)
            a = b
            b = c
    return b


def fib_mem(n):
    global memo
    if n < 2:
        result = n
    elif n in memo:
        result = memo.get(n)
    else:
        result = add(fib_mem(n-1), fib_mem(n-2))
        memo[n] = result
    return result


def compute_fib(n):
    global counter
    print("--------------------")
    print("Computing the " + str(n) + "th Fibonacci Number:")
    print("The closed form finds: " + str(fib_closed(n)))
    print("The recursive definition finds: " + str(fib_classic(n)))
    print("Additions needed for recursive definition: " + str(counter))
    reset_counter()
    print("The loop definition finds: " + str(fib_loop(n)))
    print("Additions needed for loop definition: " + str(counter))
    reset_counter()
    print("The memoization definition finds: " + str(fib_mem(n)))
    print("Additions needed for memoization definition: " + str(counter))
    reset_counter()


if __name__ == "__main__":
    print("Welcome to the Fibonacci Test Program")
    print("To exit, enter a negative number.")
    while True:
        print("Enter Fibonacci Number to compute:")
        number = int(input())
        if number < 0:
            break
        else:
            compute_fib(number)
