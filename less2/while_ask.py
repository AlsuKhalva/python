ask_user_answers = {'Как дела?': 'Хорошо', 'Что делаешь? ': 'Программирую', 'Видел новый выпуск Малышевой? ': 'Нет', 'Будешь? ': 'Буду'}


def ask_user():
    answer = input('Как дела? ')
    while answer != 'Хорошо':
        answer = input('Как дела? ')

#asc_user()

def ask_user_dict():
    while True:
            
        question = input('Задай вопрос: ')
        if question in ask_user_answers:
            a = ask_user_answers.get(question)
            print(a)
        else:
            print('Ответа нет')
            return
        
    

ask_user_dict()
print('Пока')