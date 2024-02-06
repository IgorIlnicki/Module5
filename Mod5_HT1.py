# def caching_fibonacci(nn):
#     cache = []
#     fibonacci(nn, cache)
def fibonacci(nn, cache):
            count = len(cache)
            if len(cache)<2:
                cache = [0, 1]
            # Отримати наступні числа у списку 
            if (int(cache[count-2])+int(cache[count-1])) < nn:
                cache = cache + [int(cache[count-2])+int(cache[count-1])]
                return fibonacci(nn, cache) # викликати рекурсивно функцію
            else:
                return print("cache = ", cache) # якщо досягнуто кінець, то звичайний вихід
            # return cache
print("До якого числа знайти числа Фібоначчі ?:")
nn = int(input())
cache = []
fibonacci(nn, cache)
# caching_fibonacci(nn)
# print("cache = ", cache)

