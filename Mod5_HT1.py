
def caching_fibonacci():
    cache = {}  #словник cache для зберігання результатів обчислення
    def fibonacci(n):
        if n == 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # print(" 1 cache = ", cache)
        return cache[n]
        
    return fibonacci(n)

def main(n):
    fib = caching_fibonacci()
    print(f"Числo Фібоначчі для {n}: {fib}")

n = int(input())
if __name__ == '__main__':
    main(n)


