def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(b)
        a, b = b, a + b
    return result

def golden_ratio(numbers):
    a = numbers[-2]
    b = numbers[-1]
    return b / a

def main(n):
    fib_numbers = fibonacci(n)
    print("Fibonacci numbers:", fib_numbers)
    ratio = golden_ratio(fib_numbers)
    print("Golden ratio:", ratio)

if __name__ == "__main__":
    main(10)
