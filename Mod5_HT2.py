
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
char1 = 0
def generator_numbers(text: str):
    elements = text.split()
    print(f" elements =  {elements}")
    for element in elements:
        print(f" element =  {element}")
    # print(f" element2 =  {elements[7]}")
        if element.isdigit():
            print(f"Так")
            element = int(element)
            print(f" element3 =  {element}")
            # char1 = char1 + char
        # yield 
    # print(f" char1 = {char1}")
# def msum_profit(text: str, func: Callable):
generator_numbers(text)

