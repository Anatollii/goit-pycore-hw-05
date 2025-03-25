def caching_fibonacci():
    cash = {}
    def fibonacci(n):
        if n <= 0: # базовий випадок
            return 0
        if n == 1: # другий базовий випадок
            return 1
        if n in cash: # якщо є в cash відразу повернути
            return cash[n]

        print(f"Розраховую fibonacci({n})")
        cash[n] = fibonacci(n-1) + fibonacci(n-2)
        return cash[n]
    return fibonacci #замикання



fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610