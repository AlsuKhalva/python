from collections import Counter

phones = ["iPhone Xs", "Samsung Galaxy S10", "Xiaomi Mi8", "iPhone Xs", "iPhone Xs", "Xiaomi Mi8"]
count = Counter(phones)

print(count)
Counter({'iPhone Xs': 3, 'Xiaomi Mi8': 2, 'Samsung Galaxy S10': 1})

print(count['iPhone Xs'])