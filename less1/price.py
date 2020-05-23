def format_price(price):
    price = int(price)
    return (f'Цена: {price} руб.')

format = format_price(56.24)
print(format)




# price = 100
# discount = 5

# price_with_discount = price - price * discount / 100

# print(price_with_discount)


# def discounted(price, discount, max_discount=50):
#    price = abs(float(price))
#    discount = abs(float(discount))
#    max_discount = abs(float(max_discount))
#    if max_discount > 99:
#        raise ValueError('WTF! Максимальная скидка не более 99%')
#    if discount >= max_discount:
#        price_with_discount = price
#    else:
#        price_with_discount = price - price * discount / 100

#    return price_with_discount

# product = {
#    'name': 'Samsung Galaxy S10',
#    'stock': 8,
#    'price': 50000.0,
#    'discount': 50}

# product['with_discount'] = discounted(product['price'], product['discount'])

# print(product)