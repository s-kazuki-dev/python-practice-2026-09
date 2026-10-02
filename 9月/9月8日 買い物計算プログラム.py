products = [
    {"name": "りんご", "price": 150, "stock": 10},
    {"name": "みかん", "price": 100, "stock": 8},
    {"name": "バナナ", "price": 200, "stock": 5}
]

def show_products(products):
    for i in range(len(products)):
        print(f'{i+1}:{products[i]["name"]} {products[i]["price"]}円 在庫{products[i]["stock"]}個')

def buy_product(product, how_many):
    if how_many <= 0 :
        print('1個以上入力してください')
        return False
    elif product["stock"] >= how_many :
        product["stock"] -= how_many
        pay_money = product["price"] * how_many
        print(f'{product["name"]}を{how_many}個購入しました')
        print(f'お支払い金額は{pay_money}円です')
        print(f'在庫は{product["stock"]}個です')
        return True
    else:
        print(f'在庫が足りません')
        return False

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

show_products(products)

while True :
    product_number = input_integer('商品番号を入力してください(0で終了)')
    if product_number == 0:
        break
    elif  1 <= product_number <= len(products):
        selected_product = products[product_number-1]
        print(f'{selected_product["name"]}を選択しました')
        print(f'価格は{selected_product["price"]}円です')
        print(f'在庫は{selected_product["stock"]}個です')
        while True:
            how_many = input_integer('何個購入しますか？(0でキャンセル)')
            if how_many == 0:
                break
            if buy_product(selected_product, how_many):
                show_products(products)
                break  
    else:
        print('正しい商品番号を入力してください')
        
