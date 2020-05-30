

def ask_user():
    try:
        answer = input('Как дела? ')
        while answer != 'Хорошо':
            answer = input('Как дела? ')
            break
    except KeyboardInterrupt:
        print('Пока =(')
    

ask_user()

