a=2.0
b='2.0'
c=2
d= True
e= None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


name= input('Введите ваше имя: ')
print(f'Привет,  {name}!')


a='Привет'
b='мир'
d=2
c= '{}, {}{}!'.format(a, b, d)
print(c)

user = 'Python'
c = 'Привет, {name}!'.format(name=user)
print(c)

a='Привет'
b='мир'
c= f'{a}, {b}!'
d=len(c)
print(d)

a= 'привет'.upper()
print(a)

b= 'МИР'.lower()
print(b)

c= 'python'.capitalize()
print(c)

a= '  Алсу   '
b=a.strip()
print(b)

a= 'Прив3т т3б3!'
b=a.replace('3', 'е')
print(a)
print(b)

a= 'Привет приветЫ'.lower().replace('ы', '').capitalize()
print(a)


a= 'learn.python.ru'
print(a.split('.'))

a='Привет из    нескольких   слов 123  '
b= a.split()
print(b)
print(len(b))

a = None
b =0
print(a is None)
print(b is None)