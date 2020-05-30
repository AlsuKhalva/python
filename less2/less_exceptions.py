def cut_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит {z} пирога')
    except ZeroDivisionError:
        print('Не надо делить на 0!')
    except TypeError:
        print('Вы можете ввести только число')

cut_cake('111')