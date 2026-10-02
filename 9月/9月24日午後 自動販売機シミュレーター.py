products = [
    {"name": "水", "price": 100, "stock": 3},
    {"name": "お茶", "price": 130, "stock": 2},
    {"name": "コーヒー", "price": 150, "stock": 0}
]

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def input_add_money():
    while True:
        money = input_integer('投入金額を入力/0でキャンセル:')
        if money == 0:
            return
        elif money < 0:
            print('正しい金額を入力してください')
        else:
            return money

def show_products(products):
    if not products:
        print('商品はありません')
        return
    for number, product in enumerate(products, start=1):
        print(f'{number}.{product["name"]}:{product["price"]}円:在庫{product["stock"]}本')

def buy_product(product, money):
    product["stock"] -= 1
    remaining_money = money - product["price"]
    return remaining_money

def run_buy_products(products):
    if not products:
        print('商品はありません')
        return
    money = input_add_money()
    if not money:
        return
    while True:
        print('------------------------')
        show_products(products)
        print('0.終了')
        print('------------------------')
        number = input_integer('商品番号を入力/0でキャンセル:')
        if number == 0:
            print(f'おつり:{money}円')
            print('ありがとうございました')
            return
        elif 1 <= number <= len(products):
            product = products[number-1]
            if product["stock"] == 0:
                print('在庫がありません')
                continue
            if money < product["price"]:
                print('金額が足りません')
                continue
            money = buy_product(product, money)
        else:
            print('正しい番号を入力してください')
            continue  
        print(f'{product["name"]}を購入しました')
        print(f'残金{money}円')

run_buy_products(products)


