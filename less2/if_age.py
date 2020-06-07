
def how_old(age):
    if age <= 6:
        return 'Посещает детский сад'
    elif 6 < age <= 17:
        return 'Учится в школе'
    elif 17 < age <= 23:
        return 'Учится в ВУЗе'
    else:
        return 'Работает на работе работником'

age = input('Сколько Вам лет? ')
age = float(age) 

what_are_you_doing = how_old(age)
print(what_are_you_doing)