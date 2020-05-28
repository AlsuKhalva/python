ask_user = {'Как дела? ': 'Хорошо', 'Что делаешь? ': 'Программирую', 'Видел новый выпуск Малышевой? ': 'Нет', 'Будешь? ': 'Буду'}
ask_user = list(ask_user.keys())
print(ask_user[0])
while True:
    ask_user = input(ask_user[0])
    if ask_user ==  list(ask_user.value[0]):
        print(ask_user)
        