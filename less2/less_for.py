from less_if import discounted

stock = [
		{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

for phone in stock:
#    print(phone)
    phone['final_price'] = discounted(phone['price'], phone['discount'], name=phone['name'])
#    print(phone)
 #   print('-----------')

print(stock)



#exemple_string = 'Я изучаю язык python'

#for word in exemple_string.split():
#    print(f'Длина слова {word}: {len(word)}')


#students_scores = [1, 21, 19, 6, 5]

#print(f'Средняя оценка: {sum(students_scores)/len(students_scores)}')

#scores_sum = 0
#for score in students_scores:
#    scores_sum += score
#    print(scores_sum)

#print(f'Средняя оценка: {scores_sum/len(students_scores)}')

