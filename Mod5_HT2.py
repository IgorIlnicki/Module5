import re
from functools import reduce
from typing import Callable
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
char1 = 0
def generator_numbers(text: str):
    elements = text.split()
    print(f" elements =  {elements}")
    pattern = r"\d+\.+\d+"
    digit = list(map(float,filter(lambda x: re.findall(pattern, x), elements)))
    print(f" digit =  {digit}")
    for dig in digit:
        print(f"dig =  {dig}")
        yield dig

def sum_profit(text: str, func: Callable):
    generator_numbers(text)
    return reduce(lambda x,y:x+y ,func(text))

# generator_numbers(text)
if __name__=="__main__":
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

