import random
def res(a, b):
    if a == b:
        print('Ничья!')
    elif (a == 1 and b == 2) or (a == 2 and b == 3) \
    or (a == 3 and b == 1):
        print('Вы выиграли!')
    else:
        print('Вы проиграли..')

while True:
    print('Выберите 1 - Камень, 2 - Ножницы, 3 - Бумага: ')
    user_choice = int(input())
    if user_choice in (1, 2, 3):
        break
    else:
        print('Некорректный ввод!')
comp_choice = random.randint(1, 4)
if comp_choice == 1:
    print('Компьютер выбрал камень')
elif comp_choice == 2:
    print('Компьютер выбрал ножницы')
else:
    print('Компьютер выбрал бумагу')

res(user_choice, comp_choice)



