import json

def load_products():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            products = json.load(file)
        return products
    except FileNotFoundError:
        return []

def save_products(products):
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=2)

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def input_positive_integer(message):
    while True:
        number = input_integer(message)  
        if number <= 0:
            print('1以上で入力してください')
        else:
            return number

def input_non_negative_integer(message):
    while True:
        number =input_integer(message)
        if number < 0:
            print('0以上で入力してください')
        else:
            return number
        
def show_products(products):
    if not products:
        print('商品はありません')
        return
    for i in range(len(products)):
        print(f'{i+1}:{products[i]["name"]} {products[i]["price"]}円 在庫{products[i]["stock"]}個')

def add_product(products, name ,price, stock):
    products.append({
        "name":name, "price":price, "stock":stock
    })
    save_products(products)

def input_product(products):
    name = input('商品名を入力')
    price = input_positive_integer('価格を入力')
    stock = input_non_negative_integer('在庫数を入力')
    add_product(products,name,price,stock)

def select_product(products,product_number):
    if 1 <= product_number <= len(products):
        return products[product_number-1]
    else:
        return None

def restock_product(product,amount):
    product["stock"] += amount

def input_restock(products):
    if not products:
        print('商品がありません')
        return 
    show_products(products)
    while True:
        product_number = input_positive_integer('商品番号を入力')
        product = select_product(products,product_number)
        if product is None:
            print('正しい番号を入力してください')
        else:
            amount = input_positive_integer('入荷数を入力')
            restock_product(product, amount)
            save_products(products)
            show_products(products)
            break

def sell_product(product,amount):
    if product["stock"] >= amount:
        product["stock"] -= amount
        return True
    else:
        return False

def input_sell(products):
    if not products:
        print('商品がありません')
        return
    show_products(products)
    while True:
        product_number = input_positive_integer('商品番号を入力')
        product = select_product(products, product_number)
        if product is None:
            print('正しい番号を入力してください')
        else:  
            sell_amount = input_positive_integer('販売数を入力')
            if sell_product(product,sell_amount):
                print('販売しました')
                save_products(products)
            else:
                print('在庫が足りません')
            show_products(products)    
            break

def delete_product(products, product_number):
    if 1<= product_number <= len(products):
        del products[product_number-1]
        return True
    else:
        return False

def input_delete_product(products):
    if not products:
        print('商品がありません')
        return
    show_products(products)
    number = input_positive_integer('削除する商品番号を入力')
    if delete_product(products,number):
        print('削除しました')
        save_products(products)
    else:
        print('正しい番号を入力してください')
    show_products(products)

def run_inventory_manager(products):
    while True:
        print('---------------------------')
        print('1.商品一覧')
        print('2.商品追加')
        print('3.入荷')
        print('4.販売')
        print('5.商品削除')
        print('0.終了')
        print('---------------------------')
        number = input_non_negative_integer('番号を入力')
        if number == 1:
            show_products(products)
        elif number == 2:
            input_product(products)
        elif number == 3:
            input_restock(products)
        elif number == 4:
            input_sell(products)
        elif number == 5:
            input_delete_product(products)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

products = load_products()
run_inventory_manager(products)

