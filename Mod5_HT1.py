# def caching_fibonacci(nn):
#     cache = []
#     fibonacci(nn, cache)
# def fibonacci(nn, cache):
#             count = len(cache)
#             if len(cache)<2:
#                 cache = [0, 1]
#             # Отримати наступні числа у списку 
#             if (int(cache[count-2])+int(cache[count-1])) < nn:
#                 cache = cache + [int(cache[count-2])+int(cache[count-1])]
#                 return fibonacci(nn, cache) # викликати рекурсивно функцію
#             else:
#                 return print("cache = ", cache) # якщо досягнуто кінець, то звичайний вихід
#             # return cache
# print("До якого числа знайти числа Фібоначчі ?:")
# nn = int(input())
# cache = []
# fibonacci(nn, cache)
# # caching_fibonacci(nn)
# # print("cache = ", cache)
def caching_fibonacci():
    cache = []
    print(f"n = {n} cache = {cache}")
    def fibonacci(n, cache) -> int:
        count = len(cache)
        if len(cache)<2:
            cache = [0, 1]
            print(f"2   n = {n} cache = {cache}")
            print(f"3 cache[0] = {cache[0]} cache[{1}] = {cache[1]}")
            print(f"5 cache[{count-2}] = {cache[count-2]} cache[{count-1}] = {cache[count-1]}")
            # Отримати наступні числа у списку 
            b = int(cache[count-2]) + int(cache[count-1])
            print(f"6 b = {b}")
        if b < n:
            cache.append(b)
            print(f"7   n = {n} cache = {cache}")
            return fibonacci(n, cache) # викликати рекурсивно функцію
        else:
            return print("cache = ", cache) # якщо досягнуто кінець, то звичайний вихід
    return fibonacci(n, cache)

def main(n):
    # print(f"{cache}") 
    fib = caching_fibonacci()
    print(f"Числа Фібоначчі для {n}: {fib}")

n = int(input())
if __name__ == '__main__':
    main(n)


