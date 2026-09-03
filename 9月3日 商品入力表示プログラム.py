prices = [1200, 800, 1500]

sum_prices = 0

for i in prices:
    sum_prices += i

print(f'合計金額は{sum_prices}円です')


counts = 0

for price in prices:

    if price >= 1000:
        counts += 1

print(f'1000円以上の商品は{counts}個です')


new_sum_prices = 0

for price in prices :

    if price >= 1000 :
        new_sum_prices += price

print(f'1000円以上の商品の合計は{new_sum_prices}円です')


new_prices = [1200, 800, 1500, 500, 2000]

new_counts = 0
new_sum_prices = 0

for new_price in new_prices :
    if new_price >= 1000:
        new_counts += 1
        new_sum_prices += new_price

print(f'1000円以上の商品は{new_counts}個です')
print(f'1000円以上の商品の合計は{new_sum_prices}円です')


user_prices = []
sum_user_prices = 0
for i in range(3):
    user_prices.append (int(input(f'{i+1}つ目の商品の値段を入力してください')))

for user_price in user_prices:
    sum_user_prices += user_price

print(f'入力された価格:{user_prices}')
print(f'合計金額は{sum_user_prices} 円です')


user_prices = []
total_prices = 0

for i in range(3):
    user_prices.append(int(input(f'{i+1}つ目の商品の値段を入力してください')))

count_over_1000 = 0
total_over_1000 = 0
for price in user_prices:
    total_prices += price
    if price >= 1000 :
        count_over_1000 += 1
        total_over_1000 += price

print(f'入力された価格は:{user_prices}')
print(f'全商品の合計は{total_prices}円です')
print(f'1000円以上の商品は{count_over_1000}個です')
print(f'1000円以上の商品の合計は{total_over_1000}円です')

