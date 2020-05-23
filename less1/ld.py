a = [3, 5, 7, 9, 10.5]
print(a)

a.append('Python')
print(a)

b = len(a)
print(b)


print(a[0])
print(a[-1])
print(a[2:5])
a.remove('Python')
print(a)


prognoz = {
    'city': 'Москва',
    'temperature': '20'}

print(prognoz['temperature'])
prognoz['temperature'] = int(prognoz['temperature']) - 5
print(prognoz)

print(prognoz.get('country', 'Россия'))

prognoz['date '] = '27.05.2019'
print(len(prognoz))