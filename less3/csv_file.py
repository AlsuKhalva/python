import csv


employees_list = [
                {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
                {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
                {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            ]

with open('export.csv', 'w', encoding='utf-8') as empl:

    column = ['name', 'age', 'job']
    empl_writer = csv.DictWriter(empl, column, delimiter=';')
    empl_writer.writeheader()

    for employee in employees_list:
        empl_writer.writerow(employee)