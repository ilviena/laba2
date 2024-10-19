def get_number():
    for number in range(30):
        if number % 2 != 0:
            yield number
numbers = get_number()
lst = list(numbers)
first = lst[0]
fifth = lst[4]
last = lst[-1]
print('Первое, пятое и последнее значения: ', first, ', ', fifth, ', ', last)
