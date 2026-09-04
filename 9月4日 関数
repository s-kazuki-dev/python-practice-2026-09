def calculate_total(prices):
    sum_price = 0
    for price in prices:
        sum_price += price

    return sum_price

prices = [1200, 800, 1500, 500, 2000]

total = calculate_total(prices)

print(f'合計金額は{total}円です')


def count_over_1000(prices):
    counts = 0
    for price in prices :
        if price >= 1000:
            counts += 1
    return counts

count = count_over_1000(prices)

print(f'1000円以上の商品は{count}個です')


def total_over_1000(prices):
    sum_over_1000 = 0
    for price in prices :
        if price >= 1000 :
            sum_over_1000 += price
    return sum_over_1000

total = total_over_1000(prices)

print(f'1000円以上の商品の合計は{total}円です')


def total_over_price(prices,number):
    sum_over_number = 0
    for price in prices :
        if price >= number :
            sum_over_number += price
    return sum_over_number

total = total_over_price(prices,1500)

print(f'1500円以上の商品の合計が{total}円です')


def count_over_price(prices,number):
    counts = 0
    for price in prices :
        if price >= number :
            counts += 1
    return counts

count = count_over_price(prices,1500)

print(f'1500円以上の商品は{count}個です')


prices = []
for i in range(3):
    prices.append(int(input(f'{i+1}つ目の商品価格を入力してください')))

standard_price = int(input('基準金額を入力してください'))

print(f'入力された価格:{prices}')
print(f'{standard_price}円以上の商品は{count_over_price(prices,standard_price)}個です')
print(f'{standard_price}円以上の商品の合計は{total_over_price(prices,standard_price)}円です')

