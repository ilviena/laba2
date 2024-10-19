from datetime import datetime

def calc_age():
    while True:
        birthday_str = input("Введите дату рождения дд/мм/гггг: ")
        
        if len(birthday_str) == 10 and birthday_str[2] == '/' and birthday_str[5] == '/':
            day = int(birthday_str[:2])
            month = int(birthday_str[3:5])
            year = int(birthday_str[6:])

            if (month >= 1) and (month <= 12):
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    max_day = 31
                elif month in [4, 6, 9, 11]:
                    max_day = 30
                else:
                    max_day = 29
                
                if (day >= 1) and (day <= max_day):
                    break
                else:
                    print("Неверный день!")
            else:
                print("Неверный месяц!")
        else:
            print("Неверный ввод! Формат должен быть дд/мм/гггг")

    birthday = datetime(year, month, day)
    today = datetime.now()
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    
    print("Ваш возраст - ", age, "лет")

calc_age()
