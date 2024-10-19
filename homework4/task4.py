import random
gen_numbers = [random.randint(0, 200) for i in range(10)]
print("Сгенерированные числа: ", gen_numbers)
kr_numbers = []
while True:
    x = (input("Введите цифру X: "))
    if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        x = int(x)
        break
    else:
        print("Цифра должна быть от 1 до 9.")
def filter(numbers, func):
    for number in numbers:
        if func(number):
            kr_numbers.append(number)
filter(gen_numbers, lambda a: a%x == 0)
if kr_numbers:
    print("Числа, кратные", x, ": ", kr_numbers)
else:
    print("Нет чисел, кратных ", x, ":(")