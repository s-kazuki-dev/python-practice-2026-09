import json

def load_sales():
    try:
        with open("sales.json", "r", encoding="utf-8") as file:
            sales = json.load(file)
            return sales
    except FileNotFoundError:
        return []

def save_sales(sales):
    with open("sales.json", "w", encoding="utf-8") as file:
        json.dump(sales, file, ensure_ascii=False, indent=2)

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
        if number < 1:
            print('1以上で入力してください')
        else:
            return number

def calculate_total_sales(sales):
    total = 0
    for sale in sales:
        total += sale["price"] * sale["quantity"]
    return total

def calculate_product_sales(sales,product_name):
    total = 0
    for sale in sales:
        if product_name == sale["name"]:
            total += sale["price"] * sale["quantity"]
    return total

def product_exists(sales,product_name):
    for sale in sales:
        if sale["name"] == product_name:
            return True
    return False

def search_product_sales(sales):
    if not sales:
            print('売上データがありません')
            return
    product_name = input('商品名を入力:')
    if not product_exists(sales,product_name):
        print('該当する商品がありません')
    else:
        total = calculate_product_sales(sales,product_name)
        print(f'{product_name}の売上:{total}円')

def calculate_sales_by_product(sales):
    totals = {}
    for sale in sales:
        if sale["name"] not in totals:
            totals[sale["name"]] = sale["price"] * sale["quantity"]
        else:
            totals[sale["name"]] += sale["price"] * sale["quantity"]
    return totals

def find_top_product(totals):
    max_name = None
    max_sales = 0
    for product_name in totals:
        if totals[product_name] > max_sales:
            max_sales = totals[product_name]
            max_name = product_name
    return max_name, max_sales

def calculate_quantity_by_product(sales):
    totals ={}
    for sale in sales:
        if sale["name"] not in totals:
            totals[sale["name"]] = sale["quantity"]
        else:
            totals[sale["name"]] += sale["quantity"]
    return totals

def find_top_quantity(quantity_totals):
    max_name = None
    max_quantity = 0
    for product_name in quantity_totals:
        if quantity_totals[product_name] > max_quantity:
            max_quantity = quantity_totals[product_name]
            max_name = product_name
    return max_name, max_quantity

def show_sales_report(sales):
    if not sales:
        print('売上データがありません')
        return
    total = calculate_total_sales(sales)
    print(f'総売上:{total}円')
    print('---------------')
    print('商品別売上')
    totals =calculate_sales_by_product(sales)
    for product_name in totals:
        print(f'{product_name}:{totals[product_name]}円')
    print('----------------')
    top_name, top_sales =find_top_product(totals)
    print(f'最高売上商品:{top_name} {top_sales}円')
    quantity_totals = calculate_quantity_by_product(sales)
    top_quantity_name, top_quantity = find_top_quantity(quantity_totals)
    print(f'最多販売商品:{top_quantity_name} {top_quantity}個')

def add_sale(sales,name,price,quantity):
    sales.append({
        "name":name,
        "price":price,
        "quantity":quantity
    })
    save_sales(sales)

def input_sale(sales):
    name = input('商品名を入力:')
    price = input_positive_integer('価格を入力:')
    quantity = input_positive_integer('個数を入力')
    add_sale(sales,name,price,quantity)
    print('販売記録を追加しました')

def run_sales_analyzer(sales):
    while True:
        print('------------------------')
        print('------------------------')
        print('1.売上レポート')
        print('2.商品売上検索')
        print('3.販売記録追加')
        print('0.終了')
        print('------------------------')
        print('------------------------')
        number = input_integer('番号を入力')
        if number == 1:
            show_sales_report(sales)
        elif number == 2:
            search_product_sales(sales)
        elif number == 3:
            input_sale(sales)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

sales = load_sales()
run_sales_analyzer(sales)

