prices = [1200, 800, 1500, 500, 2000]

def calculate_average(prices):
    sum_prices = 0
    for price in prices :
        sum_prices += price
    return sum_prices / len(prices)

average = calculate_average(prices)
print(f'商品の平均価格は{average}円です')    


counts_over_average = 0
for price in prices:
    if price >= average:
        counts_over_average += 1

print(f'平均以上の商品は{counts_over_average}個です')


def count_over_average(prices):
    counts = 0
    average = calculate_average(prices)
    for price in prices :
        if price >= average:
            counts += 1
    return counts

print(f'平均以上の商品の個数は{count_over_average(prices)}個です')


def total_over_average(prices):
    sum_price = 0
    average = calculate_average(prices)
    for price in prices:
        if price >= average:
            sum_price += price
    return sum_price

print(f'平均以上の商品の合計は{total_over_average(prices)}円です')


def get_prices_over_average(prices):
    average = calculate_average(prices)
    new_prices = []
    for price in prices:
        if price >= average:
            new_prices.append(price)
    return new_prices

print(f'平均以上の商品のリスト:{get_prices_over_average(prices)}')


product = {"name":"りんご",
           "price":150,
           "stock":10
}
print(f'商品名:{product["name"]}')
print(f'価格:{product["price"]}円')
print(f'在庫:{product["stock"]}個')

product["stock"] -= 1
print(f'りんごを1個購入しました')
print(f'残り在庫は{product["stock"]}個です')


how_many = int(input('何個購入しますか？'))
product["stock"] -= how_many
print(f'りんごを{how_many}個購入しました')
print(f'残り在庫は{product["stock"]}個です')


how_many = int(input('何個購入しますか？'))
stock = product["stock"] - how_many
if stock >= 0:
    product["stock"] = stock
    print(f'残り在庫は{stock}個です')
else:
    print('在庫が足りません')


product = {"name":"りんご",
           "price":150,
           "stock":10
}
how_many = int(input('何個購入しますか？'))
if product["stock"] >= how_many and how_many >= 1:
    product["stock"] -= how_many
    pay_money = how_many * product["price"]
    print(f'りんごを{how_many}個購入しました')
    print(f'お支払い金額は{pay_money}円です')
    print(f'残り在庫は{product["stock"]}個です')
elif how_many <= 0:
    print('1個以上入力してください')
else:
    print(f'在庫が足りません')


product = {"name":"りんご",
           "price":150,
           "stock":10
}
how_many = int(input('何個購入しますか？'))
if how_many <= 0:
    print('1個以上入力してください')
elif product["stock"] >= how_many:
    product["stock"] -= how_many
    pay_money = how_many * product["price"]
    print(f'{product["name"]}を{how_many}個購入しました')
    print(f'お支払い金額は{pay_money}円です')
    print(f'残り在庫は{product["stock"]}個です')
else:
    print(f'在庫が足りません')


def buy_product(product, how_many):
    if how_many <= 0:
        print('1個以上入力してください')
    elif product["stock"] >= how_many:
        product["stock"] -= how_many
        pay_money = how_many * product["price"]
        print(f'{product["name"]}を{how_many}個購入しました')
        print(f'お支払い金額は{pay_money}円です')
        print(f'残り在庫は{product["stock"]}個です')
    else:
        print(f'在庫が足りません')

product = {
    "name":"りんご",
    "price":150,
    "stock":10
}

how_many = int(input('何個購入しますか？'))

buy_product(product,how_many)

print('---------------------------')

products = [
    {"name":"りんご", "price":150, "stock":10},
    {"name":"みかん", "price":100, "stock":8},
    {"name":"バナナ", "price":200, "stock":5}
]

print(f'1:{products[0]["name"]} {products[0]["price"]}円 在庫{products[0]["stock"]}個')
print(f'2:{products[1]["name"]} {products[1]["price"]}円 在庫{products[1]["stock"]}個')
print(f'3:{products[2]["name"]} {products[2]["price"]}円 在庫{products[2]["stock"]}個')

number = int(input('商品番号を入力してください')) - 1
how_many = int(input('何個購入しますか？'))

buy_product(products[number], how_many)


for i in range(len(products)):
    print(f'{i+1}:{products[i]["name"]} {products[i]["price"]}円 在庫{products[i]["stock"]}個')


print('---------------------------------------------')

products = [
    {"name":"りんご", "price":150, "stock":10},
    {"name":"みかん", "price":100, "stock":8},
    {"name":"バナナ", "price":200, "stock":5}
]

for i in range(len(products)):
    print(f'{i+1}:{products[i]["name"]} {products[i]["price"]}円 在庫{products[i]["stock"]}個')

number = int(input('商品番号を入力してください')) - 1

if 0 <= number < len(products):
    how_many = int(input('何個購入しますか？'))
    buy_product(products[number], how_many)
else:
    print('正しい商品番号を入力してください')
      