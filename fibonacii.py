def fibonacci(n):
    fib_sequence = []
    a , b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a , b = b, a + b
    return fib_sequence

n = int((input("Enter the Number: ")))
fib_sequence = fibonacci(n)

print(f"The First {n} Fibonacci numbers are: {fib_sequence}")